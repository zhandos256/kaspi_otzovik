FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -U pip && pip3 install -r requirements.txt

COPY . /app/

ENV BOT_TOKEN=7692919718:AAH0myJyR66DbGjQvc9Bl1YBeCHOl-nnyjs

CMD [ "sh", "-c", "/app/init.sh && python /app/src/main.py" ]