"""Health check and monitoring endpoints."""

from .health import router as health_router
from .metrics import router as metrics_router
from .version import router as version_router

__all__ = [
    "health_router",
    "metrics_router",
    "version_router",
]
