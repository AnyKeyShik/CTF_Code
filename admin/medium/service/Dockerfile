FROM python:3-onbuild
ENV PYTHONUNBUFFERED 1

CMD [ "gunicorn", "main:app", "--config", "gunicorn.conf.py" ]
