FROM python:3.12-alpine

WORKDIR /src/

COPY . /src/
COPY start_commands.sh /start_commands.sh
RUN chmod +x /start_commands.sh

RUN apk add --no-cache bash
SHELL ["/bin/bash", "-c"]
RUN pip install -r requirements.txt
