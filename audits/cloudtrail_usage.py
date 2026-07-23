from datetime import datetime, timedelta, timezone
from collections import defaultdict
def run(session, regions, days=90):
    rows=[]; usage=defaultdict(lambda:{"EventCount":0,"LastUsed":""})
    start=datetime.now(timezone.utc)-timedelta(days=days); end=datetime.now(timezone.utc)
    for region in regions:
        try:
            ct=session.client("cloudtrail", region_name=region)
            paginator=ct.get_paginator("lookup_events")
            for page in paginator.paginate(StartTime=start, EndTime=end):
                for ev in page.get("Events",[]):
                    src=ev.get("EventSource","unknown")
                    usage[src]["EventCount"]+=1
                    t=str(ev.get("EventTime",""))
                    if t>usage[src]["LastUsed"]: usage[src]["LastUsed"]=t
        except Exception as e:
            rows.append({"Service":"CloudTrail","Region":region,"Error":str(e)})
    for src,meta in usage.items():
        rows.append({"ServiceEventSource":src,"EventCountLastNDays":meta["EventCount"],"LastUsed":meta["LastUsed"]})
    return rows
