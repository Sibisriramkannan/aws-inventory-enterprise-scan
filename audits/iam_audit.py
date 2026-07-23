def run(session):
    rows=[]
    try:
        iam=session.client("iam")
        for u in iam.list_users().get("Users",[]):
            username=u.get("UserName")
            try: mfa=iam.list_mfa_devices(UserName=username).get("MFADevices",[])
            except Exception: mfa=[]
            try: keys=iam.list_access_keys(UserName=username).get("AccessKeyMetadata",[])
            except Exception: keys=[]
            rows.append({"UserName":username,"MFAEnabled":bool(mfa),"AccessKeyCount":len(keys),"PasswordLastUsed":str(u.get("PasswordLastUsed","")),"CreateDate":str(u.get("CreateDate","")),"Risk":"High" if not mfa else "Low","Recommendation":"Enable MFA" if not mfa else "OK"})
    except Exception as e: rows.append({"Error":str(e)})
    return rows
