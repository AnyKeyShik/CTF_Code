FROM python:3.8-alpine

RUN mkdir -p /app
WORKDIR /app

RUN apk add socat

COPY . /app

USER nobody

ENV PYTHONUNBUFFERED=1

CMD ["socat", "TCP4-LISTEN:7777,reuseaddr,fork", "EXEC:timeout 60 ./server.py"]
