FROM ubuntu:latest

RUN apt-get update && \
	apt-get upgrade -yyq && \
    DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata && \
	apt-get install golang -yyq

RUN mkdir -p /app
WORKDIR /app

COPY . /app
RUN go build -o server main.go

ENTRYPOINT ./server
