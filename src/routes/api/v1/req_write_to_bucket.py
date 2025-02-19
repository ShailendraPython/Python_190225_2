import json

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse, Response
from src.models.proxy import ProxyRequest
from src.services.httpbin import proxy_request
from settings import settings
from clients.gcs_client import GCSBucketClient

router = APIRouter(tags=["Greetings"], prefix="/api/v1")


@router.post(
    "/hello",
    summary="Write to Bucket",
    response_model=dict,
    status_code=status.HTTP_201_CREATED
)
async def request_write_to_bucket(request: ProxyRequest):
    """

    """
    # Call the proxy_request function
    response = await proxy_request(request)

    # If response is already a JSONResponse, extract the JSON data
    response_content = json.loads(response.body.decode())
    content = response_content.get("json", {})
    file_name =  content.get("name",'Test') + str(content.get("test_number" , "0")) + ".jsom"
    GCSBucketClient.write_to_bucket(bucket_name=settings.gcsbucket.bucket_name, file_name=file_name, file_content=content)
    # If response is a dict, return it directly
    return Response(status_code=status.HTTP_201_CREATED)
