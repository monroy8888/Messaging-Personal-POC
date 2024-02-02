from pydantic import BaseModel
from enum import Enum
from pydantic import BaseModel
from fastapi import Form, UploadFile, File
from typing import Dict, List, Optional


class UploadResponse(BaseModel):
    filename: str
    option: List[str] = ["si", "no"]

    def json(self):
        return {
            "filename": self.filename,
            "option": self.option,
        }


class FunctionType(str, Enum):
    option1 = "option1"
    option2 = "option2"
    option3 = "option3"


class MessageRequest(BaseModel):
    regEx: List
    headers: List

class MessageResponse(BaseModel):
    result: str