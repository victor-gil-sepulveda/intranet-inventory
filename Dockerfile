FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.8

COPY ./app /app

COPY requirements.txt /app

ENV UWSGI_CHEAPER 4

ENV UWSGI_PROCESSES 64

ENV NGINX_WORKER_PROCESSES 2

ENV PYTHONPATH "${PYTHONPATH}:/app"

COPY ./sfw/zint-2.4.2.tar.gz zint-2.4.2.tar.gz

COPY ./sfw/install.sh install.sh

RUN pip install -r /app/requirements.txt

RUN apk add --update make cmake build-base

RUN chmod +x install.sh;\
    tar -xvf zint-2.4.2.tar.gz;\
    cd zint-2.4.2;\
    ls;\
    ../install.sh;\
    rm -rf /var/cache/apk/*
