FROM python:3.6.6-alpine

RUN mkdir -p /app
WORKDIR /app

COPY . /app

RUN python3 -m pip install --proxy http://172.16.1.10:3128 -r requirements.txt

USER nobody

ENV PYTHONUNBUFFERED 1

CMD [ "gunicorn", "main:app", "--config", "gunicorn.conf.py" ]
