FROM python:3.10-slim-buster


RUN apt-get update \
    && apt-get -y install netcat gcc \
    && rm -rf /var/lib/apt/lists/* 

WORKDIR /api
# COPY alembic.ini .
# COPY tune_alembic.sh .
# RUN chmod +x /api/tune_alembic.sh 

COPY Pipfile .

RUN python -m pip install pipenv \ 
    && pipenv lock \
    && pipenv install --system 


COPY . .


EXPOSE 8083