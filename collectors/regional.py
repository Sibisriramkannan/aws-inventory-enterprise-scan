from utils import paginate, tags_to_string, get_name, error_row

def collect_ec2(session, region):
    rows, errors=[], []
    try:
        c=session.client("ec2", region_name=region)
        for r in paginate(c,"describe_instances","Reservations"):
            for i in r.get("Instances",[]):
                rows.append({"Region":region,"InstanceId":i.get("InstanceId"),"Name":get_name(i.get("Tags")),"State":i.get("State",{}).get("Name"),"InstanceType":i.get("InstanceType"),"Platform":i.get("Platform","Linux/UNIX"),"PrivateIp":i.get("PrivateIpAddress"),"PublicIp":i.get("PublicIpAddress"),"VpcId":i.get("VpcId"),"SubnetId":i.get("SubnetId"),"KeyName":i.get("KeyName"),"LaunchTime":str(i.get("LaunchTime","")),"SecurityGroups":str(i.get("SecurityGroups",[])),"Tags":tags_to_string(i.get("Tags"))})
    except Exception as e: errors.append(error_row("EC2",region,e))
    return rows, errors

def collect_ebs(session, region):
    rows, errors=[], []
    try:
        c=session.client("ec2", region_name=region)
        for v in paginate(c,"describe_volumes","Volumes"):
            rows.append({"Region":region,"VolumeId":v.get("VolumeId"),"Name":get_name(v.get("Tags")),"SizeGB":v.get("Size"),"VolumeType":v.get("VolumeType"),"State":v.get("State"),"Encrypted":v.get("Encrypted"),"AvailabilityZone":v.get("AvailabilityZone"),"Attachments":str(v.get("Attachments",[])),"CreateTime":str(v.get("CreateTime","")),"Tags":tags_to_string(v.get("Tags"))})
    except Exception as e: errors.append(error_row("EBS",region,e))
    return rows, errors

def collect_ami(session, region):
    rows, errors=[], []
    try:
        c=session.client("ec2", region_name=region)
        for a in paginate(c,"describe_images","Images",Owners=["self"]):
            rows.append({"Region":region,"ImageId":a.get("ImageId"),"Name":a.get("Name"),"State":a.get("State"),"CreationDate":a.get("CreationDate"),"Architecture":a.get("Architecture"),"RootDeviceType":a.get("RootDeviceType"),"VirtualizationType":a.get("VirtualizationType"),"Tags":tags_to_string(a.get("Tags"))})
    except Exception as e: errors.append(error_row("AMI",region,e))
    return rows, errors

def collect_vpc(session, region):
    rows, errors=[], []
    try:
        c=session.client("ec2", region_name=region)
        for v in paginate(c,"describe_vpcs","Vpcs"):
            rows.append({"Region":region,"VpcId":v.get("VpcId"),"Name":get_name(v.get("Tags")),"CidrBlock":v.get("CidrBlock"),"State":v.get("State"),"IsDefault":v.get("IsDefault"),"Tags":tags_to_string(v.get("Tags"))})
    except Exception as e: errors.append(error_row("VPC",region,e))
    return rows, errors

def collect_subnets(session, region):
    rows, errors=[], []
    try:
        c=session.client("ec2", region_name=region)
        for s in paginate(c,"describe_subnets","Subnets"):
            rows.append({"Region":region,"SubnetId":s.get("SubnetId"),"Name":get_name(s.get("Tags")),"VpcId":s.get("VpcId"),"CidrBlock":s.get("CidrBlock"),"AvailabilityZone":s.get("AvailabilityZone"),"AvailableIpAddressCount":s.get("AvailableIpAddressCount"),"MapPublicIpOnLaunch":s.get("MapPublicIpOnLaunch"),"DefaultForAz":s.get("DefaultForAz"),"Tags":tags_to_string(s.get("Tags"))})
    except Exception as e: errors.append(error_row("Subnets",region,e))
    return rows, errors

def collect_route_tables(session, region):
    rows, errors=[], []
    try:
        c=session.client("ec2", region_name=region)
        for rt in paginate(c,"describe_route_tables","RouteTables"):
            rows.append({"Region":region,"RouteTableId":rt.get("RouteTableId"),"Name":get_name(rt.get("Tags")),"VpcId":rt.get("VpcId"),"Routes":str(rt.get("Routes",[])),"Associations":str(rt.get("Associations",[])),"Tags":tags_to_string(rt.get("Tags"))})
    except Exception as e: errors.append(error_row("RouteTables",region,e))
    return rows, errors

def collect_igw(session, region):
    rows, errors=[], []
    try:
        c=session.client("ec2", region_name=region)
        for i in paginate(c,"describe_internet_gateways","InternetGateways"):
            rows.append({"Region":region,"InternetGatewayId":i.get("InternetGatewayId"),"Name":get_name(i.get("Tags")),"Attachments":str(i.get("Attachments",[])),"Tags":tags_to_string(i.get("Tags"))})
    except Exception as e: errors.append(error_row("InternetGateways",region,e))
    return rows, errors

def collect_nat(session, region):
    rows, errors=[], []
    try:
        c=session.client("ec2", region_name=region)
        for n in paginate(c,"describe_nat_gateways","NatGateways"):
            rows.append({"Region":region,"NatGatewayId":n.get("NatGatewayId"),"VpcId":n.get("VpcId"),"SubnetId":n.get("SubnetId"),"State":n.get("State"),"ConnectivityType":n.get("ConnectivityType"),"NatGatewayAddresses":str(n.get("NatGatewayAddresses",[])),"CreateTime":str(n.get("CreateTime","")),"Tags":tags_to_string(n.get("Tags"))})
    except Exception as e: errors.append(error_row("NATGateways",region,e))
    return rows, errors

def collect_security_groups(session, region):
    rows, errors=[], []
    try:
        c=session.client("ec2", region_name=region)
        for sg in paginate(c,"describe_security_groups","SecurityGroups"):
            rows.append({"Region":region,"GroupId":sg.get("GroupId"),"GroupName":sg.get("GroupName"),"Description":sg.get("Description"),"VpcId":sg.get("VpcId"),"InboundRules":str(sg.get("IpPermissions",[])),"OutboundRules":str(sg.get("IpPermissionsEgress",[])),"Tags":tags_to_string(sg.get("Tags"))})
    except Exception as e: errors.append(error_row("SecurityGroups",region,e))
    return rows, errors

def collect_nacl(session, region):
    rows, errors=[], []
    try:
        c=session.client("ec2", region_name=region)
        for n in paginate(c,"describe_network_acls","NetworkAcls"):
            rows.append({"Region":region,"NetworkAclId":n.get("NetworkAclId"),"VpcId":n.get("VpcId"),"IsDefault":n.get("IsDefault"),"Entries":str(n.get("Entries",[])),"Associations":str(n.get("Associations",[])),"Tags":tags_to_string(n.get("Tags"))})
    except Exception as e: errors.append(error_row("NACL",region,e))
    return rows, errors

def collect_efs(session, region):
    rows, errors=[], []
    try:
        c=session.client("efs", region_name=region)
        for fs in paginate(c,"describe_file_systems","FileSystems"):
            rows.append({"Region":region,"FileSystemId":fs.get("FileSystemId"),"Name":fs.get("Name"),"LifeCycleState":fs.get("LifeCycleState"),"Encrypted":fs.get("Encrypted"),"PerformanceMode":fs.get("PerformanceMode"),"ThroughputMode":fs.get("ThroughputMode"),"SizeBytes":fs.get("SizeInBytes",{}).get("Value"),"CreationTime":str(fs.get("CreationTime",""))})
    except Exception as e: errors.append(error_row("EFS",region,e))
    return rows, errors

def collect_fsx(session, region):
    rows, errors=[], []
    try:
        c=session.client("fsx", region_name=region)
        for fs in paginate(c,"describe_file_systems","FileSystems"):
            rows.append({"Region":region,"FileSystemId":fs.get("FileSystemId"),"FileSystemType":fs.get("FileSystemType"),"Lifecycle":fs.get("Lifecycle"),"StorageCapacity":fs.get("StorageCapacity"),"StorageType":fs.get("StorageType"),"VpcId":fs.get("VpcId"),"SubnetIds":str(fs.get("SubnetIds",[])),"Tags":tags_to_string(fs.get("Tags"))})
    except Exception as e: errors.append(error_row("FSx",region,e))
    return rows, errors

def collect_rds(session, region):
    rows, errors=[], []
    try:
        c=session.client("rds", region_name=region)
        for db in paginate(c,"describe_db_instances","DBInstances"):
            rows.append({"Region":region,"DBInstanceIdentifier":db.get("DBInstanceIdentifier"),"Engine":db.get("Engine"),"EngineVersion":db.get("EngineVersion"),"DBInstanceClass":db.get("DBInstanceClass"),"Status":db.get("DBInstanceStatus"),"MultiAZ":db.get("MultiAZ"),"StorageEncrypted":db.get("StorageEncrypted"),"AllocatedStorage":db.get("AllocatedStorage"),"Endpoint":str(db.get("Endpoint",{})),"VpcId":db.get("DBSubnetGroup",{}).get("VpcId")})
    except Exception as e: errors.append(error_row("RDS",region,e))
    return rows, errors

def collect_dynamodb(session, region):
    rows, errors=[], []
    try:
        c=session.client("dynamodb", region_name=region)
        for page in paginate(c,"list_tables"):
            for name in page.get("TableNames",[]):
                try:
                    t=c.describe_table(TableName=name).get("Table",{})
                    rows.append({"Region":region,"TableName":name,"TableStatus":t.get("TableStatus"),"BillingMode":t.get("BillingModeSummary",{}).get("BillingMode"),"ItemCount":t.get("ItemCount"),"TableSizeBytes":t.get("TableSizeBytes"),"CreationDateTime":str(t.get("CreationDateTime",""))})
                except Exception as inner: errors.append(error_row("DynamoDB",region,inner))
    except Exception as e: errors.append(error_row("DynamoDB",region,e))
    return rows, errors

def collect_redshift(session, region):
    rows, errors=[], []
    try:
        c=session.client("redshift", region_name=region)
        for x in paginate(c,"describe_clusters","Clusters"):
            rows.append({"Region":region,"ClusterIdentifier":x.get("ClusterIdentifier"),"NodeType":x.get("NodeType"),"ClusterStatus":x.get("ClusterStatus"),"DBName":x.get("DBName"),"NumberOfNodes":x.get("NumberOfNodes"),"Encrypted":x.get("Encrypted"),"VpcId":x.get("VpcId")})
    except Exception as e: errors.append(error_row("Redshift",region,e))
    return rows, errors

def collect_elasticache(session, region):
    rows, errors=[], []
    try:
        c=session.client("elasticache", region_name=region)
        for x in paginate(c,"describe_cache_clusters","CacheClusters",ShowCacheNodeInfo=True):
            rows.append({"Region":region,"CacheClusterId":x.get("CacheClusterId"),"Engine":x.get("Engine"),"CacheClusterStatus":x.get("CacheClusterStatus"),"CacheNodeType":x.get("CacheNodeType"),"NumCacheNodes":x.get("NumCacheNodes"),"PreferredAvailabilityZone":x.get("PreferredAvailabilityZone")})
    except Exception as e: errors.append(error_row("ElastiCache",region,e))
    return rows, errors

def collect_ecs(session, region):
    rows, errors=[], []
    try:
        c=session.client("ecs", region_name=region)
        arns=[]
        for page in paginate(c,"list_clusters"): arns.extend(page.get("clusterArns",[]))
        for i in range(0,len(arns),100):
            for x in c.describe_clusters(clusters=arns[i:i+100]).get("clusters",[]):
                rows.append({"Region":region,"ClusterName":x.get("clusterName"),"ClusterArn":x.get("clusterArn"),"Status":x.get("status"),"RunningTasks":x.get("runningTasksCount"),"PendingTasks":x.get("pendingTasksCount"),"ActiveServices":x.get("activeServicesCount")})
    except Exception as e: errors.append(error_row("ECS",region,e))
    return rows, errors

def collect_eks(session, region):
    rows, errors=[], []
    try:
        c=session.client("eks", region_name=region)
        for page in paginate(c,"list_clusters"):
            for name in page.get("clusters",[]):
                try:
                    x=c.describe_cluster(name=name).get("cluster",{})
                    rows.append({"Region":region,"ClusterName":name,"Status":x.get("status"),"Version":x.get("version"),"Endpoint":x.get("endpoint"),"RoleArn":x.get("roleArn"),"VpcConfig":str(x.get("resourcesVpcConfig",{}))})
                except Exception as inner: errors.append(error_row("EKS",region,inner))
    except Exception as e: errors.append(error_row("EKS",region,e))
    return rows, errors

def collect_ecr(session, region):
    rows, errors=[], []
    try:
        c=session.client("ecr", region_name=region)
        for r in paginate(c,"describe_repositories","repositories"):
            rows.append({"Region":region,"RepositoryName":r.get("repositoryName"),"RepositoryUri":r.get("repositoryUri"),"CreatedAt":str(r.get("createdAt","")),"ImageScanning":str(r.get("imageScanningConfiguration",{})),"Encryption":str(r.get("encryptionConfiguration",{}))})
    except Exception as e: errors.append(error_row("ECR",region,e))
    return rows, errors

def collect_lambda(session, region):
    rows, errors=[], []
    try:
        c=session.client("lambda", region_name=region)
        for f in paginate(c,"list_functions","Functions"):
            rows.append({"Region":region,"FunctionName":f.get("FunctionName"),"Runtime":f.get("Runtime"),"Handler":f.get("Handler"),"CodeSize":f.get("CodeSize"),"Timeout":f.get("Timeout"),"MemorySize":f.get("MemorySize"),"LastModified":f.get("LastModified"),"Role":f.get("Role")})
    except Exception as e: errors.append(error_row("Lambda",region,e))
    return rows, errors

def collect_autoscaling(session, region):
    rows, errors=[], []
    try:
        c=session.client("autoscaling", region_name=region)
        for g in paginate(c,"describe_auto_scaling_groups","AutoScalingGroups"):
            rows.append({"Region":region,"AutoScalingGroupName":g.get("AutoScalingGroupName"),"MinSize":g.get("MinSize"),"MaxSize":g.get("MaxSize"),"DesiredCapacity":g.get("DesiredCapacity"),"Instances":str(g.get("Instances",[])),"VPCZoneIdentifier":g.get("VPCZoneIdentifier"),"HealthCheckType":g.get("HealthCheckType")})
    except Exception as e: errors.append(error_row("AutoScaling",region,e))
    return rows, errors

def collect_elb(session, region):
    rows, errors=[], []
    try:
        c=session.client("elbv2", region_name=region)
        for lb in paginate(c,"describe_load_balancers","LoadBalancers"):
            rows.append({"Region":region,"Name":lb.get("LoadBalancerName"),"Arn":lb.get("LoadBalancerArn"),"Type":lb.get("Type"),"Scheme":lb.get("Scheme"),"DNSName":lb.get("DNSName"),"State":lb.get("State",{}).get("Code"),"VpcId":lb.get("VpcId"),"AvailabilityZones":str(lb.get("AvailabilityZones",[]))})
    except Exception as e: errors.append(error_row("ELBv2",region,e))
    try:
        c=session.client("elb", region_name=region)
        for lb in paginate(c,"describe_load_balancers","LoadBalancerDescriptions"):
            rows.append({"Region":region,"Name":lb.get("LoadBalancerName"),"Arn":"","Type":"classic","Scheme":lb.get("Scheme"),"DNSName":lb.get("DNSName"),"State":"","VpcId":lb.get("VPCId"),"AvailabilityZones":str(lb.get("AvailabilityZones",[]))})
    except Exception as e: errors.append(error_row("ClassicELB",region,e))
    return rows, errors

def collect_cloudwatch(session, region):
    rows, errors=[], []
    try:
        c=session.client("cloudwatch", region_name=region)
        for a in paginate(c,"describe_alarms","MetricAlarms"):
            rows.append({"Region":region,"AlarmName":a.get("AlarmName"),"StateValue":a.get("StateValue"),"MetricName":a.get("MetricName"),"Namespace":a.get("Namespace"),"Statistic":a.get("Statistic"),"Threshold":a.get("Threshold"),"ComparisonOperator":a.get("ComparisonOperator")})
    except Exception as e: errors.append(error_row("CloudWatchAlarms",region,e))
    return rows, errors

def collect_sns(session, region):
    rows, errors=[], []
    try:
        c=session.client("sns", region_name=region)
        for t in paginate(c,"list_topics","Topics"):
            rows.append({"Region":region,"TopicArn":t.get("TopicArn")})
    except Exception as e: errors.append(error_row("SNS",region,e))
    return rows, errors

def collect_sqs(session, region):
    rows, errors=[], []
    try:
        c=session.client("sqs", region_name=region)
        for url in c.list_queues().get("QueueUrls",[]):
            attrs=c.get_queue_attributes(QueueUrl=url,AttributeNames=["All"]).get("Attributes",{})
            rows.append({"Region":region,"QueueUrl":url,"QueueName":url.split("/")[-1],"MessagesAvailable":attrs.get("ApproximateNumberOfMessages"),"VisibilityTimeout":attrs.get("VisibilityTimeout"),"CreatedTimestamp":attrs.get("CreatedTimestamp")})
    except Exception as e: errors.append(error_row("SQS",region,e))
    return rows, errors

def collect_cloudformation(session, region):
    rows, errors=[], []
    try:
        c=session.client("cloudformation", region_name=region)
        for s in paginate(c,"describe_stacks","Stacks"):
            rows.append({"Region":region,"StackName":s.get("StackName"),"StackId":s.get("StackId"),"Status":s.get("StackStatus"),"CreationTime":str(s.get("CreationTime","")),"Description":s.get("Description")})
    except Exception as e: errors.append(error_row("CloudFormation",region,e))
    return rows, errors

def collect_codepipeline(session, region):
    rows, errors=[], []
    try:
        c=session.client("codepipeline", region_name=region)
        for p in paginate(c,"list_pipelines","pipelines"):
            rows.append({"Region":region,"Name":p.get("name"),"Version":p.get("version"),"Created":str(p.get("created","")),"Updated":str(p.get("updated",""))})
    except Exception as e: errors.append(error_row("CodePipeline",region,e))
    return rows, errors

def collect_codebuild(session, region):
    rows, errors=[], []
    try:
        c=session.client("codebuild", region_name=region)
        names=c.list_projects().get("projects",[])
        for i in range(0,len(names),100):
            for p in c.batch_get_projects(names=names[i:i+100]).get("projects",[]):
                rows.append({"Region":region,"Name":p.get("name"),"Arn":p.get("arn"),"SourceType":p.get("source",{}).get("type"),"EnvironmentType":p.get("environment",{}).get("type"),"ServiceRole":p.get("serviceRole"),"Created":str(p.get("created",""))})
    except Exception as e: errors.append(error_row("CodeBuild",region,e))
    return rows, errors

def collect_codedeploy(session, region):
    rows, errors=[], []
    try:
        c=session.client("codedeploy", region_name=region)
        for page in paginate(c,"list_applications"):
            for app in page.get("applications",[]): rows.append({"Region":region,"ApplicationName":app})
    except Exception as e: errors.append(error_row("CodeDeploy",region,e))
    return rows, errors
