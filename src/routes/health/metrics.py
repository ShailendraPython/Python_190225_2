"""Prometheus metrics endpoint."""

from fastapi import APIRouter, Response, HTTPException
from prometheus_client import (
    generate_latest,
    CONTENT_TYPE_LATEST,
    Gauge,
    Counter,
    Histogram,
)
import psutil
import asyncio


router = APIRouter(tags=["Health"])

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "status"],
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["method", "endpoint"],
)

MEMORY_USAGE = Gauge("memory_usage_bytes", "Memory usage in bytes")

CPU_USAGE = Gauge("cpu_usage_percent", "CPU usage percentage")


async def update_system_metrics():
    """Update system metrics in a non-blocking way."""
    try:
        metrics = await asyncio.to_thread(
            lambda: {
                "memory": psutil.Process().memory_info().rss,
                "cpu": psutil.cpu_percent(),
            }
        )
        MEMORY_USAGE.set(metrics["memory"])
        CPU_USAGE.set(metrics["cpu"])
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to update system metrics: {str(e)}"
        )


@router.get(
    "/metrics",
    response_class=Response,
    summary="Get service metrics",
    description="Returns service metrics in Prometheus format",
)
async def metrics() -> Response:
    """Expose service metrics in Prometheus format."""
    await update_system_metrics()
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)
