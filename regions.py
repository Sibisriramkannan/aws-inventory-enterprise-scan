def get_enabled_regions(session):
    ec2=session.client("ec2", region_name="us-east-1")
    return sorted([r["RegionName"] for r in ec2.describe_regions(AllRegions=False).get("Regions",[])])
