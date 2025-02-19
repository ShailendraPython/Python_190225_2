"""API v1 endpoints."""

from .hello import router as hello_router
from .goodbye import router as goodbye_router
from .req_write_to_bucket import router as proxy_router

__all__ = [
    "hello_router",
    "goodbye_router",
    "proxy_router",
]
