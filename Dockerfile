FROM python:3.12-alpine

WORKDIR /src/

COPY . /src/

RUN pip install -r requirements.txt