import os
import logging
import hashlib
from fastapi import UploadFile
from datetime import datetime


class MainServices:

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.upload_dir = os.getenv("UPLOADS_DIR", "uploads")

    async def upload_file(self, uploaded_file: UploadFile):
        """

        :return:
        """
        file_content = uploaded_file.filename
        encrypt_file_name = await self.encrypt_file_name(file_content)
        file_path = await self.create_path(encrypt_file_name)

        with open(file_path, 'wb') as file:
            data = uploaded_file.file.read()
            file.write(data)

        return {"message": "File uploaded successfully",
                "path": file_path}

    async def create_path(self, file_content):
        uploads_dir = self.upload_dir

        os.makedirs(uploads_dir, exist_ok=True)
        file_path = os.path.join(uploads_dir, file_content)
        self.log.info(f"FILE PATH: {file_path}")

        return file_path

    async def encrypt_file_name(self, uploaded_file_name: str) -> str:
        hash_name = hashlib.sha256(uploaded_file_name.encode()).hexdigest()
        current_date = datetime.now().strftime("%Y%m%d%H%M%S")
        self.log.info(f"{hash_name[:10]}_{uploaded_file_name}_{current_date}")
        return f"{hash_name[:10]}_{uploaded_file_name}_{current_date}"


