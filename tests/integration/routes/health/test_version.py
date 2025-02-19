"""Integration tests for version endpoint."""

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


class TestVersionEndpoint:
    @pytest.mark.asyncio
    async def test_version_endpoint(self, async_client):
        response = await async_client.get("/version")
        assert response.status_code == 200
        data = response.json()
        assert all(
            k in data for k in ["git_commit", "build_timestamp", "build_log_url"]
        )
