"""Health check endpoints for service liveness."""

from fastapi import APIRouter
from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str

    class Config:
        json_schema_extra = {"example": {"status": "ok"}}


router = APIRouter(tags=["Health"])


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Health check endpoint",
    description="Returns status of service health",
)
async def health_check() -> HealthResponse:
    """Basic health check endpoint."""
    return HealthResponse(status="ok")
