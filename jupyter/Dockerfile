FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y python3 python3-pip git curl && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    pip install --upgrade pip

WORKDIR /home/base/work

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -ms /bin/bash base
USER base

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--NotebookApp.token=''"]