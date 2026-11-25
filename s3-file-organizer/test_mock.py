import boto3
from moto import mock_aws
from s3_organizer import organize_and_upload

BUCKET = "test-bucket"
FOLDER = "files-to-upload"

with mock_aws():
    s3 = boto3.client("s3", region_name="ap-south-1")
    s3.create_bucket(
        Bucket=BUCKET,
        CreateBucketConfiguration={"LocationConstraint": "ap-south-1"},
    )

    total = organize_and_upload(s3, BUCKET, FOLDER)
    print("Total files uploaded:", total)

    print("\nBucket contents:")
    response = s3.list_objects_v2(Bucket=BUCKET)
    for obj in response.get("Contents", []):
        print(" ", obj["Key"], obj["Size"], "bytes")