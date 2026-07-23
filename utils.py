import datetime
def tags_to_string(tags):
    if not tags: return ""
    return "; ".join([f"{t.get('Key')}={t.get('Value')}" for t in tags if isinstance(t,dict)])
def get_name(tags):
    for t in tags or []:
        if t.get("Key")=="Name": return t.get("Value","")
    return ""
def error_row(service, region, error): return {"Service":service,"Region":region,"Error":str(error)}
def paginate(client, operation_name, result_key=None, **kwargs):
    try:
        paginator=client.get_paginator(operation_name)
        for page in paginator.paginate(**kwargs):
            if result_key:
                for item in page.get(result_key,[]): yield item
            else:
                yield page
    except Exception:
        resp=getattr(client, operation_name)(**kwargs)
        if result_key:
            for item in resp.get(result_key,[]): yield item
        else:
            yield resp
