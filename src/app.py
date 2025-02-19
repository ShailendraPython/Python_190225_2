"""FastAPI application factory and server configuration."""
import logging

import uvicorn
from fastapi import FastAPI
#from x35_json_logging import initialize_logging


from routes.api.v1 import hello as hello_v1
from routes.api.v1 import req_write_to_bucket

from settings import settings

# initialize_logging()
logger = logging.getLogger(f"x35.{__name__}")


def create_app() -> FastAPI:
    app = FastAPI(
        docs_url="/docs" if settings.fastapi.enable_docs else None,
        redoc_url="/redoc" if settings.fastapi.enable_docs else None,
    )

    # Application routes
    app.include_router(hello_v1.router)
    app.include_router(req_write_to_bucket.router)

    return app


if __name__ == "__main__":
    logger.info("Starting FastAPI application")
    uvicorn.run(
        "app:create_app",
        factory=True,
        access_log=settings.uvicorn.access_log,
        backlog=settings.uvicorn.backlog,
        host="0.0.0.0",
        http=settings.uvicorn.http,
        limit_concurrency=settings.uvicorn.max_concurrency,
        log_level=settings.uvicorn.log_level,
        loop=settings.uvicorn.loop,
        port=settings.uvicorn.port,
        proxy_headers=settings.uvicorn.proxy_headers,
        reload=settings.uvicorn.reload,
        server_header=settings.uvicorn.server_header,
        timeout_keep_alive=settings.uvicorn.keep_alive,
        workers=settings.uvicorn.workers,
    )
