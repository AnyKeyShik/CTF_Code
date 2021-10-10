FROM ubuntu:latest

RUN apt-get update && \
    apt-get upgrade -yyq && \
    apt-get install build-essential libelf-dev libc6-dev binutils-dev libdwarf-dev -yyq

ADD . /task
WORKDIR /task
RUN make

CMD ./pingme
