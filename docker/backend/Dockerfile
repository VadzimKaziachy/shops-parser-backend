FROM python:3.8

COPY Pipfile ./
COPY Pipfile.lock ./

RUN apt-get update && \
    apt-get install -y postgresql-client && \
    pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system

