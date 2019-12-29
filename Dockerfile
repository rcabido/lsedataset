FROM ubuntu:16.04

WORKDIR /usr/src/lsedataset

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY Requirements.txt ./

RUN pip3 install -r Requirements.txt

COPY bugPytube.sh ./
COPY mixins.py ./

RUN sh bugPytube.sh
 
COPY sample/ sample/
COPY data/ data/

