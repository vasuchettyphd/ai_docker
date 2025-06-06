FROM nvidia/cuda:12.1.1-base-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3.10 python3-pip python3-venv \
    build-essential curl git ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash base
WORKDIR /home/base
COPY requirements.txt ./

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

RUN mkdir -p /home/base/.local/share/jupyter/runtime && \
    chown -R base:base /home/base

USER base

EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--ServerApp.token=''", "--ServerApp.allow_origin='*'", "--ServerApp.allow_remote_access=True"]