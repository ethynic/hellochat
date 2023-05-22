FROM python:3.10-alpine

ENV FLASK_APP flasky.py
ENV FLASK_CONFIG docker

WORKDIR /home/flasky

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install gunicorn
RUN venv/bin/pip install -r requirements.txt
COPY app app
COPY migrations migrations
COPY flasky.py config.py boot.sh data.sqlite ./
<<<<<<< HEAD
RUN chmod +x ./boot.sh
=======
RUN mv boot.sh entrypoint.sh && chmod +x ./entrypoint.sh
>>>>>>> 65197bf53d551626f38579de1982d746dadb8be4

EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]
