FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -U pip && pip3 install -r requirements.txt

COPY . /app/

ENV BOT_TOKEN=""

RUN chmod +x run.sh

CMD [ "sh", "-c", "/app/run.sh" ]