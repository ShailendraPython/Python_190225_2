from .fastapi import FastAPISettings
from .uvicorn import UvicornSettings
from .gcsbucket import GCSBucketSettings


class Settings:
    """
    Unified settings class combining Base, FastAPI, and Uvicorn settings.

    Provides a single point of access to all configuration.
    """

    def __init__(self):
        self.fastapi = FastAPISettings()
        self.uvicorn = UvicornSettings()
        self.gcsbucket = GCSBucketSettings()


settings = Settings()
