from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class GCSBucketSettings(BaseSettings):
    bucket_name: str = Field(
        default="test-python-shailen"

    )