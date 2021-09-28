FROM python:2.7-alpine

RUN mkdir -p /app
WORKDIR /app

RUN apk add socat
RUN python2 -m pip install secretsharing

COPY . /app

USER nobody

ENV PYTHONUNBUFFERED=1

CMD ["socat", "TCP4-LISTEN:7777,reuseaddr,fork", "EXEC:timeout 60 ./server.py"]
