FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

RUN apt-get install wget apt-utils lsb-core cmake git -y && \
    apt-get install libopencv-dev -y 

RUN useradd -ms /bin/bash lse
USER lse
WORKDIR /home/lse

COPY Requirements.txt ./
COPY lsedataset/ lsedataset/

RUN pip3 install -r Requirements.txt

COPY bugPytube.sh ./
COPY __main__.py ./
COPY playlist.py ./

RUN sh bugPytube.sh

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

RUN locale-gen es_ES.UTF-8
ENV LANG es_ES.UTF-8
ENV LANGUAGE es_ES:es
ENV LC_ALL es_ES.UTF-8

RUN sudo apt-get update && \
    sudo apt-get -y install ffmpeg
WORKDIR ../../
COPY lsedataset/ lsedataset/
WORKDIR lsedataset/
USER root
ENTRYPOINT ["python3"]
CMD ["lsedataset.py"]
