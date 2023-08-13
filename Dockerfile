FROM python:3.8-slim

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "python3" , "nba_stats_puller.py" ]