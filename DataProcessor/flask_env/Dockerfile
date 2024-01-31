FROM python:2.7 as base_python

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./app/

CMD ["python", "app/main.py"]
