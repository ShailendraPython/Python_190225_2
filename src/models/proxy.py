from pydantic import BaseModel


class ProxyRequest(BaseModel):
    message: str
    name: str | None = None
    test_number: int | None = None
