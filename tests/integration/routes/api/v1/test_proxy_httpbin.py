"""Integration tests for v1 proxy-httpbin endpoint."""

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from src.app import create_app


@pytest_asyncio.fixture
async def async_client():
    """
    Create an async test client for the FastAPI app.
    Routes requests to the FastAPI app without actual networking.
    """
    app = create_app()
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as client:
        yield client


class TestProxyHttpbinEndpoint:
    @pytest.mark.asyncio
    async def test_proxy_request(self, async_client):
        """
        Test a valid proxy request to the endpoint.
        """
        test_data = {"message": "test message", "name": "test name", "test_number": 42}

        response = await async_client.post("/api/v1/proxy-httpbin", json=test_data)
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_proxy_invalid_request(self, async_client):
        """
        Test an invalid proxy request with incorrect data types.
        """
        invalid_data = {"message": 123, "name": "test"}  # 'message' should be a string

        response = await async_client.post("/api/v1/proxy-httpbin", json=invalid_data)
        assert response.status_code == 422
