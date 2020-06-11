FROM python:3.6

RUN apt-get update && \
  apt-get install -y postgresql \
  postgresql-client \
  vim

WORKDIR /api
COPY . /api
