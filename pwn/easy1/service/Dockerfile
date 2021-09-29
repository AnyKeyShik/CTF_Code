FROM python:3.8.1-alpine

RUN mkdir -p /app
WORKDIR /app

RUN apk add gcc musl-dev socat

COPY . /app

RUN gcc -O3 -o problem problem.c

USER nobody

ENV PYTHONUNBUFFERED=1

CMD ["socat", "TCP4-LISTEN:7777,reuseaddr,fork", "EXEC:timeout 60 ./master.py"]
