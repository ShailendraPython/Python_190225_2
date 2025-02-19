from cloudpathlib import GSPath
import json

class GCSBucketClient:

    def write_to_bucket(bucket_name, file_name, file_content):
        try:
            bucket_path = GSPath(f"gs://{bucket_name}")
            file_path = bucket_path / file_name
            #file_path.write_text(str(file_content))
            with file_path.open("w") as f:
                json.dump(file_content, f)
        except Exception as e:
            raise GCSBucketClientError("Failed to write the file to bucket") from e

class GCSBucketClientError(Exception):
    pass
