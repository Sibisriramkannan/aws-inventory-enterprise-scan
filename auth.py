import boto3
def create_session(profile=None, access_key=None, secret_key=None, session_token=None, region=None):
    if profile:
        return boto3.Session(profile_name=profile, region_name=region)
    if access_key and secret_key:
        return boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                             aws_session_token=session_token, region_name=region)
    return boto3.Session(region_name=region)
def validate_identity(session):
    ident=session.client("sts").get_caller_identity()
    return {"Account":ident.get("Account"),"Arn":ident.get("Arn"),"UserId":ident.get("UserId")}
