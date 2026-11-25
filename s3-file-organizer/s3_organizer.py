import os
from botocore.exceptions import ClientError, NoCredentialsError
from boto3.exceptions import S3UploadFailedError

TYPES = {
    ".jpg": "images",
    ".jpeg": "images",
    ".png": "images",
    ".pdf": "docs",
    ".txt": "docs",
    ".docx": "docs",
    ".csv": "data",
    ".zip": "archives",
}


def get_category(filename):
    extension = os.path.splitext(filename)[1].lower()
    return TYPES.get(extension, "other")


def organize_and_upload(s3, bucket, folder):
    uploaded = 0
    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if not os.path.isfile(path):
            continue
        key = get_category(name) + "/" + name
        s3.upload_file(path, bucket, key)
        print("Uploaded", name, "->", key)
        uploaded = uploaded + 1
    return uploaded


def main():
    import boto3

    bucket = "sumangala-s3-test-2026-481"
    folder = "files-to-upload"
    s3 = boto3.client("s3")

    try:
        total = organize_and_upload(s3, bucket, folder)
        print("Total files uploaded:", total)
    except FileNotFoundError:
        print("Folder not found:", folder)
    except NoCredentialsError:
        print("AWS credentials not found. Run aws configure.")
    except ClientError as error:
        print("AWS error:", error)
    except S3UploadFailedError as error:
        print("Upload failed:", error)


if __name__ == "__main__":
    main()