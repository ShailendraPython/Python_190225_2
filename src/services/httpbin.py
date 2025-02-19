import logging
from fastapi.responses import JSONResponse
from httpx import HTTPStatusError, TransportError
from src.models.proxy import ProxyRequest
from src.clients.httpx import create_httpx_client

logger = logging.getLogger(f"x35.{__name__}")


# NOTE: Client lifecycle consideration
# Currently creating a new client per request for simplicity. For high-traffic production
# scenarios, consider using a global client with FastAPI lifecycle events or more sophisticated
# client management. See Also:
#   - httpx Clients: https://www.python-httpx.org/advanced/clients/
#   - FastAPI Events: https://fastapi.tiangolo.com/advanced/events/
async def proxy_request(request: ProxyRequest):
    try:
        async with await create_httpx_client() as client:
            response = await client.post(
                "https://httpbin.org/post",
                json=request.model_dump(),
                headers={"Content-Type": "application/json"},
            )
            response.raise_for_status()
            logger.info(
                "Successfully proxied request to httpbin",
                extra={
                    "status_code": response.status_code,
                    "response_time": response.elapsed.total_seconds(),
                },
            )
            return JSONResponse(
                content=response.json(), status_code=response.status_code
            )
    except HTTPStatusError as e:
        logger.error(
            "HTTP error occurred", extra={"status_code": e.response.status_code}
        )
        return JSONResponse(
            content={"error": "Upstream service error", "details": str(e)},
            status_code=e.response.status_code,
        )
    except TransportError as e:
        logger.error("Transport error occurred", extra={"error": str(e)})
        return JSONResponse(
            content={"error": "Connection error", "details": str(e)},
            status_code=503,
        )
    except Exception as e:
        logger.error("Unexpected error occurred", extra={"error": str(e)})
        return JSONResponse(content={"error": "Internal server error"}, status_code=500)
