FROM nvidia/cuda:10.0-cudnn7-devel

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

RUN apt-get install wget nano apt-utils lsb-core git g++ make libprotobuf-dev protobuf-compiler libopencv-dev \
libgoogle-glog-dev libboost-all-dev libcaffe-cuda-dev libhdf5-dev libatlas-base-dev -y 

RUN wget https://github.com/Kitware/CMake/releases/download/v3.16.0/cmake-3.16.0-Linux-x86_64.tar.gz && \
tar xzf cmake-3.16.0-Linux-x86_64.tar.gz -C /opt && \
rm cmake-3.16.0-Linux-x86_64.tar.gz
ENV PATH="/opt/cmake-3.16.0-Linux-x86_64/bin:${PATH}"

RUN mkdir data

COPY Requirements.txt ./
COPY sample/ sample/

RUN pip3 install -r Requirements.txt

COPY bugPytube.sh ./
COPY mixins.py ./

RUN sh bugPytube.sh

RUN git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose.git

WORKDIR /openpose/build

RUN cmake -D CMAKE_INSTALL_PREFIX=/usr/local  \
    -D BUILD_CAFFE=ON \
    -D BUILD_EXAMPLES=ON \
    -D GPU_MODE=CUDA \
    -D CMAKE_BUILD_TYPE=Release \
    -D DOWNLOAD_BODY_COCO_MODEL=ON \
    -D DOWNLOAD_BODY_MPI_MODEL=ON \
    -D DOWNLOAD_HAND_MODEL=ON \
    -D DOWNLOAD_FACE_MODEL=ON .. 

RUN make -j`nproc` && \
    make install

RUN locale-gen es_ES.UTF-8
ENV LANG es_ES.UTF-8
ENV LANGUAGE es_ES:es
ENV LC_ALL es_ES.UTF-8

WORKDIR ./
