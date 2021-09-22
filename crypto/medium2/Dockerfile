FROM python:2.7

RUN python -m pip install secretsharing

WORKDIR /app
ADD server.py server.py
ADD flag.enc flag.enc
ADD key key
EXPOSE 1488

CMD ["python2", "./server.py"]
