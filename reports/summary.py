def build_summary(data, account_info, regions):
    rows=[{"Metric":"AWS Account","Value":account_info.get("Account","")},
          {"Metric":"Caller ARN","Value":account_info.get("Arn","")},
          {"Metric":"Regions Scanned","Value":len(regions)}]
    for k in sorted(data):
        if k not in ["Summary","AccountInfo","Regions","Errors"]:
            rows.append({"Metric":f"Total {k}","Value":len(data.get(k,[]))})
    return rows
