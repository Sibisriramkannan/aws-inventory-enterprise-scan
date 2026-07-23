from utils import paginate, error_row

def collect_s3(session):
    rows, errors=[], []
    try:
        s3=session.client("s3")
        for b in s3.list_buckets().get("Buckets",[]):
            name=b.get("Name")
            row={"Region":"","BucketName":name,"CreationDate":str(b.get("CreationDate","")),"Versioning":"","Encryption":"","PublicAccessBlock":"","PolicyStatus":""}
            for label, fn in [
                ("Region", lambda: s3.get_bucket_location(Bucket=name).get("LocationConstraint") or "us-east-1"),
                ("Versioning", lambda: s3.get_bucket_versioning(Bucket=name).get("Status","")),
                ("Encryption", lambda: str(s3.get_bucket_encryption(Bucket=name).get("ServerSideEncryptionConfiguration",{}))),
                ("PublicAccessBlock", lambda: str(s3.get_public_access_block(Bucket=name).get("PublicAccessBlockConfiguration",{}))),
                ("PolicyStatus", lambda: str(s3.get_bucket_policy_status(Bucket=name).get("PolicyStatus",{}))),
            ]:
                try: row[label]=fn()
                except Exception: pass
            rows.append(row)
    except Exception as e: errors.append(error_row("S3","global",e))
    return rows, errors

def collect_route53(session):
    rows, errors=[], []
    try:
        c=session.client("route53")
        for z in paginate(c,"list_hosted_zones","HostedZones"):
            rows.append({"Region":"global","HostedZoneId":z.get("Id"),"Name":z.get("Name"),"PrivateZone":z.get("Config",{}).get("PrivateZone"),"ResourceRecordSetCount":z.get("ResourceRecordSetCount")})
    except Exception as e: errors.append(error_row("Route53","global",e))
    return rows, errors

def collect_cloudfront(session):
    rows, errors=[], []
    try:
        c=session.client("cloudfront")
        for page in paginate(c,"list_distributions"):
            for d in page.get("DistributionList",{}).get("Items",[]):
                rows.append({"Region":"global","Id":d.get("Id"),"ARN":d.get("ARN"),"DomainName":d.get("DomainName"),"Status":d.get("Status"),"Enabled":d.get("Enabled"),"PriceClass":d.get("PriceClass"),"Aliases":str(d.get("Aliases",{}).get("Items",[]))})
    except Exception as e: errors.append(error_row("CloudFront","global",e))
    return rows, errors

def collect_iam(session):
    data={"IAMUsers":[],"IAMRoles":[],"IAMPolicies":[]}; errors=[]
    try:
        iam=session.client("iam")
        for u in paginate(iam,"list_users","Users"):
            data["IAMUsers"].append({"Region":"global","UserName":u.get("UserName"),"UserId":u.get("UserId"),"Arn":u.get("Arn"),"CreateDate":str(u.get("CreateDate","")),"PasswordLastUsed":str(u.get("PasswordLastUsed",""))})
        for r in paginate(iam,"list_roles","Roles"):
            data["IAMRoles"].append({"Region":"global","RoleName":r.get("RoleName"),"RoleId":r.get("RoleId"),"Arn":r.get("Arn"),"CreateDate":str(r.get("CreateDate","")),"MaxSessionDuration":r.get("MaxSessionDuration")})
        for p in paginate(iam,"list_policies","Policies",Scope="Local"):
            data["IAMPolicies"].append({"Region":"global","PolicyName":p.get("PolicyName"),"PolicyId":p.get("PolicyId"),"Arn":p.get("Arn"),"AttachmentCount":p.get("AttachmentCount"),"CreateDate":str(p.get("CreateDate","")),"UpdateDate":str(p.get("UpdateDate",""))})
    except Exception as e: errors.append(error_row("IAM","global",e))
    return data, errors
