FROM python:3.12-slim

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

WORKDIR /fast-api-app

# docker-compose
COPY ./fast-api-app/requirements.txt /fast-api-app/requirements.txt
COPY ./fast-api-app/app /fast-api-app/app

RUN pip install --no-cache-dir --upgrade -r /fast-api-app/requirements.txt

# FastAPI起動
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8081"]
