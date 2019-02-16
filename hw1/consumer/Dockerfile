FROM python:3.7.2-slim-stretch

COPY requirements.txt /app/

WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "main.py"]
