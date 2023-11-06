FROM python:3.11-slim

ENV PYTHONPATH /root
WORKDIR /root

RUN apt-get update && apt-get install -y build-essential
RUN pip install flytekit flytekitplugins-ray 'pydantic<2'
