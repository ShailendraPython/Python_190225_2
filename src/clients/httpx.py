import httpx


async def create_httpx_client():
    return httpx.AsyncClient(
        timeout=httpx.Timeout(10.0, connect=5.0),
        limits=httpx.Limits(max_keepalive_connections=5, max_connections=10),
        transport=httpx.AsyncHTTPTransport(retries=3),
    )
