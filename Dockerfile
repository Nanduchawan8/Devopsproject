FROM python:3.10-slim

WORKDIR /devops project

COPY app/requirements.txt .
RUN pip install -r requirements.txt

COPY app/ .

CMD ["python", "app.py"]