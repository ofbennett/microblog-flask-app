FROM python:3.6-alpine

RUN adduser -D ofb

WORKDIR /home/ofb

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql

COPY app app
COPY migrations migrations
COPY microblog.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP microblog.py
ENV USE_DOCKER True

RUN chown -R ofb:ofb ./
USER ofb

EXPOSE 5000
ENTRYPOINT [ "./boot.sh" ]