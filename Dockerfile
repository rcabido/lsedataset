FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

RUN apt-get install wget apt-utils lsb-core cmake git -y && \
    apt-get install libopencv-dev -y 

RUN mkdir data

COPY Requirements.txt ./
COPY sample/ sample/

RUN pip3 install -r Requirements.txt

COPY bugPytube.sh ./
COPY mixins.py ./

RUN git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose.git

WORKDIR openpose

RUN git checkout caa794cf81bed53b9e114299b715a6d972097b5b

WORKDIR scripts/ubuntu

RUN sed -i 's/\<sudo -H\>//g' install_deps.sh; \
   sed -i 's/\<sudo\>//g' install_deps.sh; \
   sed -i 's/\<easy_install pip\>//g' install_deps.sh; \
   sync; sleep 1; bash install_deps.sh

WORKDIR /openpose/build

RUN cmake -DGPU_MODE:String=CPU_ONLY \
          -DDOWNLOAD_BODY_MPI_MODEL:Bool=ON \
          -DDOWNLOAD_BODY_COCO_MODEL:Bool=ON \
          -DDOWNLOAD_FACE_MODEL:Bool=ON \
          -DDOWNLOAD_HAND_MODEL:Bool=ON \
          -DUSE_MKL:Bool=OFF \
          ..

RUN make -j`nproc`

RUN sh bugPytube.sh

ENV LANG es_ES.UTF-8
ENV LANGUAGE es_ES:es
ENV LC_ALL es_ES.UTF-8

WORKDIR ./
