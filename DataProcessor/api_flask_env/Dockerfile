FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y default-libmysqlclient-dev

COPY . ./app/
# COPY alembic .

EXPOSE 5000
ENV FLASK_APP=app/app.py
# Define el comando para ejecutar la aplicación Flask
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
