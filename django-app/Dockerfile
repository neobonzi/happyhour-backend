FROM ubuntu:16.04
MAINTAINER Damen King

COPY /src /opt/django-app/

RUN apt-get update \
  && apt-get install -y libpq-dev python3-pip python3-dev build-essential binutils libproj-dev gdal-bin curl \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
run pip install -r /opt/django-app/requirements.txt

EXPOSE 80
WORKDIR /opt/django-app/happyhour
