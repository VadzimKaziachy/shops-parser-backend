FROM python:3.9

COPY ../../src/Pipfile ./
COPY ../../src/Pipfile.lock ./

RUN apt-get update && \
    apt-get install -y postgresql-client && \
    pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system

