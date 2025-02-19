"""Example hello world endpoint."""

from fastapi import APIRouter, Query
import logging
from pydantic import BaseModel, ConfigDict
from typing import Optional


class HelloResponse(BaseModel):
    message: str

    model_config = ConfigDict(
        json_schema_extra={"example": {"message": "Hello, World!"}}
    )


router = APIRouter(tags=["Greetings"], prefix="/api/v1")
logger = logging.getLogger(f"x35.{__name__}")


@router.get(
    "/hello",
    response_model=HelloResponse,
    summary="Hello world endpoint",
    description="Returns a friendly greeting message, optionally personalized with a name",
)
async def hello(
    name: Optional[str] = Query(None, description="Name to greet"),
) -> HelloResponse:
    """Returns hello world message."""
    name = name.strip() if name else None
    subject = name or "World"
    logger.info("hello endpoint called with name: %s", subject)
    return HelloResponse(message=f"Hello, {subject}, I'm version 1!")
