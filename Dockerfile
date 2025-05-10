FROM python:latest
COPY . /app/
WORKDIR /app/
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "-m", "flask", "--app", "main", "run", "--port", "80", "--host", "0.0.0.0"]
