import argparse, yaml
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from auth import create_session, validate_identity
from regions import get_enabled_regions
from logger import setup_logger
from reports.excel_writer import write_excel
from reports.summary import build_summary
from collectors import regional as r
from collectors import global_collectors as g
from audits import security_audit, cost_optimization, iam_audit, cloudtrail_usage

REGIONAL_COLLECTORS=[
("EC2",r.collect_ec2),("EBS",r.collect_ebs),("AMI",r.collect_ami),("VPC",r.collect_vpc),
("Subnets",r.collect_subnets),("RouteTables",r.collect_route_tables),("InternetGateways",r.collect_igw),
("NATGateways",r.collect_nat),("SecurityGroups",r.collect_security_groups),("NACL",r.collect_nacl),
("EFS",r.collect_efs),("FSx",r.collect_fsx),("RDS",r.collect_rds),("DynamoDB",r.collect_dynamodb),
("Redshift",r.collect_redshift),("ElastiCache",r.collect_elasticache),("ECS",r.collect_ecs),("EKS",r.collect_eks),
("ECR",r.collect_ecr),("Lambda",r.collect_lambda),("AutoScaling",r.collect_autoscaling),("LoadBalancers",r.collect_elb),
("CloudWatchAlarms",r.collect_cloudwatch),("SNS",r.collect_sns),("SQS",r.collect_sqs),("CloudFormation",r.collect_cloudformation),
("CodePipeline",r.collect_codepipeline),("CodeBuild",r.collect_codebuild),("CodeDeploy",r.collect_codedeploy)
]

def load_config():
    if Path("config.yaml").exists():
        with open("config.yaml","r",encoding="utf-8") as f: return yaml.safe_load(f) or {}
    return {}

def args():
    p=argparse.ArgumentParser(description="AWS Enterprise Inventory Collector")
    p.add_argument("--profile"); p.add_argument("--access-key"); p.add_argument("--secret-key"); p.add_argument("--session-token")
    p.add_argument("--output"); p.add_argument("--workers",type=int); p.add_argument("--skip-cloudtrail",action="store_true")
    return p.parse_args()

def run_one(session, sheet, func, region):
    rows, errors=func(session, region)
    return sheet, rows, errors

def main():
    log=setup_logger(); a=args(); cfg=load_config()
    output=a.output or cfg.get("output_file","aws_inventory.xlsx")
    workers=a.workers or int(cfg.get("workers",8))
    session=create_session(a.profile,a.access_key,a.secret_key,a.session_token)
    log.info("Validating identity")
    account=validate_identity(session)
    log.info("Discovering regions")
    regions=get_enabled_regions(session)
    data={"AccountInfo":[account],"Regions":[{"Region":x} for x in regions],"Errors":[]}
    log.info("Running global collectors")
    rows,err=g.collect_s3(session); data["S3"]=rows; data["Errors"].extend(err)
    rows,err=g.collect_route53(session); data["Route53"]=rows; data["Errors"].extend(err)
    rows,err=g.collect_cloudfront(session); data["CloudFront"]=rows; data["Errors"].extend(err)
    iamdata,err=g.collect_iam(session); data.update(iamdata); data["Errors"].extend(err)
    log.info("Running regional collectors")
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs=[ex.submit(run_one,session,sheet,func,region) for region in regions for sheet,func in REGIONAL_COLLECTORS]
        for fut in as_completed(futs):
            sheet,rows,err=fut.result()
            data.setdefault(sheet,[]).extend(rows); data["Errors"].extend(err)
            log.info("%s +%s rows +%s errors", sheet, len(rows), len(err))
    log.info("Running audits")
    data["SecurityFindings"]=security_audit.run(data)
    data["CostOptimization"]=cost_optimization.run(data)
    data["IAMAudit"]=iam_audit.run(session)
    if cfg.get("include_cloudtrail_usage",True) and not a.skip_cloudtrail:
        data["CloudTrailUsage"]=cloudtrail_usage.run(session, regions, int(cfg.get("cloudtrail_days",90)))
    data["Summary"]=build_summary(data,account,regions)
    preferred=["Summary","AccountInfo","Regions","EC2","EBS","AMI","VPC","Subnets","RouteTables","InternetGateways","NATGateways","SecurityGroups","NACL","S3","EFS","FSx","RDS","DynamoDB","Redshift","ElastiCache","ECS","EKS","ECR","Lambda","AutoScaling","LoadBalancers","Route53","CloudFront","IAMUsers","IAMRoles","IAMPolicies","CloudWatchAlarms","SNS","SQS","CloudFormation","CodePipeline","CodeBuild","CodeDeploy","SecurityFindings","CostOptimization","IAMAudit","CloudTrailUsage","Errors"]
    ordered={k:data[k] for k in preferred if k in data}
    for k,v in data.items():
        if k not in ordered: ordered[k]=v
    write_excel(output, ordered)
    print(f"Inventory exported successfully: {output}")
if __name__=="__main__":
    main()
