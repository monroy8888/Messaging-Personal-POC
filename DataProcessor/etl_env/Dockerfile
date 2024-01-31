FROM python:3.9 as base_python

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install python-multipart

ENV UPLOADS_DIR "/app/app/uploads"

COPY . ./app/

# Ejecuta las migraciones y el servidor al iniciar el contenedor (puedes ajustar esto según tus necesidades)


