FROM python:3.7-alpine

COPY ./app /app

RUN pip install -r app/requirements.txt

WORKDIR /app
CMD python main.py