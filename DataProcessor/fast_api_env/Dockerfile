FROM python:3.11 as base_python

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install python-multipart

ENV UPLOADS_DIR "/app/app/uploads"

COPY . ./app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002", "--reload"]
