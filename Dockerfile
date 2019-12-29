FROM ubuntu:16.04

WORKDIR /usr/src/lsedataset

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

