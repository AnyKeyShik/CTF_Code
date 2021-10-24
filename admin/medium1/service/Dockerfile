FROM python:3.6.6-alpine

RUN mkdir -p /app
WORKDIR /app

COPY . /app

RUN python3 -m pip install -r requirements.txt

USER nobody

ENV PYTHONUNBUFFERED 1

CMD [ "gunicorn", "main:app", "--config", "gunicorn.conf.py" ]
