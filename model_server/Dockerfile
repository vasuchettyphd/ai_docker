FROM nvidia/cuda:12.1.1-base-ubuntu22.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.10 python3-pip python3-venv \
    git curl ca-certificates \
    build-essential cmake python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN mkdir -p /models/TheBloke_deepseek-coder-1.3b-base-GGUF && \
    curl -L -o /models/TheBloke_deepseek-coder-1.3b-base-GGUF/deepseek-coder-1.3b-base.Q4_K_M.gguf \
    https://huggingface.co/TheBloke/deepseek-coder-1.3b-base-GGUF/resolve/main/deepseek-coder-1.3b-base.Q4_K_M.gguf

COPY requirements.txt .

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
ENV CUDA_VISIBLE_DEVICES=0

CMD ["python3", "app.py"]