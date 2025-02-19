"""Version information endpoint."""

from fastapi import APIRouter
from pydantic import BaseModel
import os

router = APIRouter(tags=["Health"])


class VersionResponse(BaseModel):
    git_commit: str
    build_timestamp: str
    build_log_url: str

    class Config:
        json_schema_extra = {
            "example": {
                "git_commit": "abc123",
                "build_timestamp": "2024-12-30T12:00:00Z",
                "build_log_url": "https://github.com/org/repo/actions/runs/12345",
            }
        }


@router.get(
    "/version",
    response_model=VersionResponse,
    summary="Get service version and build information",
    description="Returns git commit, build timestamp, and build log details of the service.",
)
async def get_version() -> VersionResponse:
    """Retrieve service version and build information."""
    return VersionResponse(
        git_commit=os.getenv("GIT_COMMIT", "unknown"),
        build_timestamp=os.getenv("BUILD_TIMESTAMP", "unknown"),
        build_log_url=os.getenv("BUILD_LOG_URL", "unknown"),
    )
