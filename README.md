# S3 File Organizer

I built this small Python project while learning AWS. It takes the files in a local folder, uploads them to an Amazon S3 bucket, and sorts them into folders based on the file type.

For example, `report.pdf` ends up in `docs/report.pdf`, `photo.png` in `images/photo.png`, and `students.csv` in `data/students.csv`. Anything the script doesn't recognise goes into an `other/` folder.

## What it does

- Reads every file from a local folder (`files-to-upload`)
- Decides the category from the file extension
- Uploads each file to S3 with Boto3, using the category as a folder prefix
- Prints each upload and the total at the end
- Shows a clear message if the folder is missing, the AWS credentials are not set, or the upload fails

## What I used

Python, Boto3, AWS S3, IAM and the AWS CLI. For testing without AWS I used moto, which fakes S3 on my laptop.

## How to run it

1. Install the libraries:
   ```
   python -m pip install boto3 "moto[s3]"
   ```
2. Connect to AWS with an IAM user that has S3 access:
   ```
   aws configure
   ```
3. Create a bucket in S3 and put its name in `s3_organizer.py`:
   ```python
   bucket = "your-bucket-name"
   ```
4. Add a few files to the `files-to-upload` folder and run:
   ```
   python s3_organizer.py
   ```

No AWS account? You can still try it with the mock test:
```
python test_mock.py
```

## Example output

```
Uploaded backup.zip -> archives/backup.zip
Uploaded notes.txt -> docs/notes.txt
Uploaded photo.png -> images/photo.png
Uploaded report.pdf -> docs/report.pdf
Uploaded students.csv -> data/students.csv
Total files uploaded: 5
```

## A few things I learned

- My keys stay in `aws configure`, never in the code or on GitHub.
- The "folders" in S3 are really just prefixes in the file name.
- My first real run failed with Access Denied because I forgot to replace the placeholder bucket name, so now I read the error message before guessing.
- Writing a mock test with moto let me check the sorting logic before touching AWS.

## Ideas for later

- Skip files that are already in the bucket
- Show the total size uploaded
- Run it automatically on a schedule
