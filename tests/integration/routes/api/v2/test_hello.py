"""Integration tests for v2 hello endpoint."""

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


class TestHelloEndpoint:
    @pytest.mark.asyncio
    async def test_hello_default(self, async_client):
        """
        Test the default behavior of the hello endpoint.
        When no name is provided, it should default to 'World'.
        """
        response = await async_client.get("/api/v2/hello")
        assert response.status_code == 200
        assert response.json() == {"message": "Yo, World, what's up! I'm version 2!"}

    @pytest.mark.asyncio
    async def test_hello_with_name(self, async_client):
        """
        Test the hello endpoint with a provided name.
        """
        response = await async_client.get("/api/v2/hello?name=Test")
        assert response.status_code == 200
        assert response.json() == {"message": "Yo, Test, what's up! I'm version 2!"}

    @pytest.mark.asyncio
    @pytest.mark.parametrize("name", ["", " ", "   "])
    async def test_hello_empty_name(self, async_client, name):
        """
        Test that empty or whitespace-only names default to 'World'.
        """
        response = await async_client.get(f"/api/v2/hello?name={name}")
        assert response.status_code == 200
        assert response.json() == {"message": "Yo, World, what's up! I'm version 2!"}
