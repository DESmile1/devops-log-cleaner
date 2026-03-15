FROM python:3.11-slim

WORKDIR /app

COPY cleaner.py .
# Create testing log directory inside the container
RUN mkdir -p /data/logs

CMD ["python", "cleaner.py"]
