FROM python:latest

COPY . /app/
WORKDIR /app/

RUN pip install -r requirements.txt

ENV FLASK_APP=main.py
ENV FLASK_ENV=production

EXPOSE 80

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
