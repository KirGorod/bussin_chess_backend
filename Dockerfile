FROM python:3.12-alpine

WORKDIR /src/

COPY . /src/

RUN apk add --no-cache bash
SHELL ["/bin/bash", "-c"]
RUN pip install -r requirements.txt
