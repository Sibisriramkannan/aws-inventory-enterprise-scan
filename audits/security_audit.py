def run(data):
    findings=[]
    for sg in data.get("SecurityGroups",[]):
        rules=sg.get("InboundRules","")
        for port,name in [(22,"SSH open to world"),(3389,"RDP open to world"),(3306,"MySQL open to world"),(5432,"PostgreSQL open to world")]:
            if "0.0.0.0/0" in rules and str(port) in rules:
                findings.append({"Severity":"High","Finding":name,"Region":sg.get("Region"),"Resource":sg.get("GroupId"),"Details":sg.get("GroupName")})
        if "0.0.0.0/0" in rules and "'IpProtocol': '-1'" in rules:
            findings.append({"Severity":"Critical","Finding":"All traffic open to world","Region":sg.get("Region"),"Resource":sg.get("GroupId"),"Details":sg.get("GroupName")})
    for b in data.get("S3",[]):
        if "IsPublic': True" in str(b.get("PolicyStatus","")) or '"IsPublic": true' in str(b.get("PolicyStatus","")):
            findings.append({"Severity":"Critical","Finding":"S3 bucket policy is public","Region":b.get("Region"),"Resource":b.get("BucketName"),"Details":b.get("PolicyStatus")})
        if not b.get("PublicAccessBlock"):
            findings.append({"Severity":"Medium","Finding":"S3 Public Access Block not detected","Region":b.get("Region"),"Resource":b.get("BucketName"),"Details":"Could not confirm block public access"})
    return findings
