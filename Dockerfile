FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.8

COPY ./app /app

COPY requirements.txt /app

ENV UWSGI_CHEAPER 4

ENV UWSGI_PROCESSES 64

ENV NGINX_WORKER_PROCESSES 2

ENV PYTHONPATH "${PYTHONPATH}:/app"

#WORKDIR /app

RUN pip install -r /app/requirements.txt

#WORKDIR /