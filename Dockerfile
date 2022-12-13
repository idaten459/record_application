FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3-pip python3-dev build-essential libpq-dev
RUN mkdir -p /usr/local/src/work
COPY requirements.txt /usr/local/src/work
WORKDIR /usr/local/src/work
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
