FROM ubuntu:latest

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf
COPY . /home/ctf

RUN chown -R root:root /home/ctf

USER ctf
CMD ./ynetd -p 7777 ./wizards
