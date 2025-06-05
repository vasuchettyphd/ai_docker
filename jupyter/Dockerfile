FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y python3 python3-pip git curl && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    pip install --upgrade pip poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /home/base/work

COPY pyproject.toml ./
RUN poetry install --only main

RUN useradd -ms /bin/bash base
USER base

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--NotebookApp.token=''"]