FROM python:3.11 as base_python

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install python-multipart


ENV UPLOADS_DIR "/app/app/uploads"

COPY . ./app/

#CMD ["python", "app/manage.py", "makemigrations"]
#CMD ["python", "app/manage.py", "migrate"]
CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]
