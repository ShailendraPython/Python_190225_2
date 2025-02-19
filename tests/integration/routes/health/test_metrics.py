"""Integration tests for metrics endpoint."""

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from src.app import create_app


@pytest_asyncio.fixture
async def async_client():
    app = create_app()
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as client:
        yield client


class TestMetricsEndpoint:
    @pytest.mark.asyncio
    async def test_metrics_endpoint(self, async_client):
        response = await async_client.get("/metrics")
        assert response.status_code == 200
        assert "memory_usage_bytes" in response.text
        assert "cpu_usage_percent" in response.text
