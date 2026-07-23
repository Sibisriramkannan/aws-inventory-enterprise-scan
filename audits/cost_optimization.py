def run(data):
    findings=[]
    for i in data.get("EC2",[]):
        if i.get("State")=="stopped":
            findings.append({"Category":"Cost Optimization","Finding":"Stopped EC2 instance","Region":i.get("Region"),"Resource":i.get("InstanceId"),"Recommendation":"Review and terminate if not required"})
    for v in data.get("EBS",[]):
        if v.get("State")=="available":
            findings.append({"Category":"Cost Optimization","Finding":"Unattached EBS volume","Region":v.get("Region"),"Resource":v.get("VolumeId"),"Recommendation":"Snapshot and delete if unused"})
    for n in data.get("NATGateways",[]):
        if n.get("State")=="available":
            findings.append({"Category":"Cost Optimization","Finding":"NAT Gateway running","Region":n.get("Region"),"Resource":n.get("NatGatewayId"),"Recommendation":"Verify usage because NAT Gateway can be costly"})
    return findings
