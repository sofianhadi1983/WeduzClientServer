FROM python:3.7.3-alpine3.8

WORKDIR /home

RUN pip3 install --upgrade pip

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py

CMD flask run --host=0.0.0.0