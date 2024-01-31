from typing import Annotated
import logging
from fastapi import APIRouter, File, UploadFile, HTTPException, status

from ..connection.rabbitmq import send_message
from ..models.main_models import UploadResponse, FunctionType, MessageResponse, MessageRequest
from ..services.main_services import MainServices


router = APIRouter()
main_service = MainServices()
log = logging.getLogger(__name__)


@router.post('/new_message/')
async def post_message(function: UploadResponse):
    function_response = send_message(function)
    return function_response


@router.post('/file_upload/')
async def post_message(message_request: bool, uploaded_file: UploadFile = File(...)):
    """
    Receive function as a string and send it to the controller.
    """

    try:
        response = await main_service.upload_file(uploaded_file)
        log.info(f"the file path {response}")
        return {"response": response}
    except Exception as e:
        log.info(f"Error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        ) from e



