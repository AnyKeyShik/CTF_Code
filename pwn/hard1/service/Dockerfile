FROM keltecc/nsjail:latest

RUN useradd -M -s /bin/false shop_user

ADD entrypoint.sh /tmp/

RUN chmod 555 /tmp/entrypoint.sh

ADD shop flag /var/service/

USER shop_user

ENTRYPOINT /tmp/entrypoint.sh
