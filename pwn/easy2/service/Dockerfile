FROM ubuntu:latest

RUN apt-get update && \
    apt-get upgrade -yyq && \
    apt-get install gcc-multilib -yyq

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf
COPY . /home/ctf

RUN chown -R root:root /home/ctf

USER ctf
CMD ./ynetd -p 7777 ./system_health_check
