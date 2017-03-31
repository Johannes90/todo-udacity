FROM python:3.6-slim
MAINTAINER Johannes Herrmann <johannes.herrmann2012@gmail.com>

WORKDIR /server

COPY requirements.txt /server/requirements.txt
RUN pip install -r requirements.txt
COPY . /server

EXPOSE 5000