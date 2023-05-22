FROM python:3.10-alpine

ENV FLASK_APP flasky.py
ENV FLASK_CONFIG docker

RUN adduser -D flasky
USER flasky

WORKDIR /home/flasky

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install gunicorn
RUN venv/bin/pip install -r requirements.txt
COPY app app
COPY migrations migrations
COPY flasky.py config.py boot.sh data.sqlite ./
RUN chmod +x ./boot.sh

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
