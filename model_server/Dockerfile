FROM nvidia/cuda:12.1.1-base-ubuntu22.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3.10 python3-pip python3-venv \
        build-essential git curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["python3", "app.py"]