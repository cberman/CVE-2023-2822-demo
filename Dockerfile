FROM python:3.9-slim-buster

RUN pip install flask

WORKDIR /app
COPY . .

CMD [ "python", "./app.py" ]
