import os
from io import BytesIO

import boto3

S3_SESSION = boto3.session.Session()
S3_CLIENT = S3_SESSION.client(
    "s3",
    endpoint_url=os.getenv("S3_ENDPOINT", ""),
    aws_access_key_id=os.getenv("S3_ACCESS_KEY", ""),
    aws_secret_access_key=os.getenv("S3_SECRET_KEY", ""),
)
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "")


def fetch_s3_object(object_key):
    in_mem_file = BytesIO()
    S3_CLIENT.download_fileobj(S3_BUCKET_NAME, object_key, in_mem_file)
    in_mem_file.seek(0)
    return in_mem_file.read()
