FROM winamd64/python:3

WORKDIR /usr/src/lsedataset

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

