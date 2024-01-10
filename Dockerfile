FROM python:3.10
WORKDIR /api
RUN apt update && apt install -y make

