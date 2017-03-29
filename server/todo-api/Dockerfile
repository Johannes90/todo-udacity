FROM python:3.6-slim
MAINTAINER Johannes Herrmann <johannes.herrmann2012@gmail.com>

WORKDIR /todo-api

COPY requirements.txt /todo-api/requirements.txt
RUN pip install -r requirements.txt
COPY . /todo-api

EXPOSE 5000