"""Example goodbye world endpoint."""

from fastapi import APIRouter, Query
import logging
from pydantic import BaseModel, ConfigDict
from typing import Optional


class GoodbyeResponse(BaseModel):
    message: str

    model_config = ConfigDict(
        json_schema_extra={"example": {"message": "Goodbye, World!"}}
    )


router = APIRouter(tags=["Greetings"], prefix="/api/v1")
logger = logging.getLogger(f"x35.{__name__}")


@router.get(
    "/goodbye",
    response_model=GoodbyeResponse,
    summary="Goodbye world endpoint",
    description="Returns a friendly goodbye message, optionally personalized with a name",
)
async def goodbye(
    name: Optional[str] = Query(None, description="Name to say goodbye to"),
) -> GoodbyeResponse:
    """Returns goodbye world message."""
    name = name.strip() if name else None
    subject = name or "World"
    logger.info("goodbye endpoint called with name: %s", subject)
    return GoodbyeResponse(message=f"Goodbye, {subject}, I'm version 1!")
