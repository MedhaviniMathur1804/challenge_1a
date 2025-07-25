FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY main.py /app/main.py

RUN apt-get update && apt-get install -y locales && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN mkdir -p /app/input /app/output

CMD ["python", "main.py"]
