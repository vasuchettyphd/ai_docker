# 📦 Requirements
* Docker 20.10+
* Docker Compose v2 (comes with Docker Desktop)
* NVIDIA GPU (e.g., RTX 2070) with 8GB+ VRAM
* NVIDIA Container Toolkit

# 🚀 Quickstart
```bash
# Clone the repo
git clone https://github.com/your-username/llama3-docker
cd llama3-docker 

# Build and start the containers
docker compose up --build
```

This will:

* Start the model server at http://localhost:5000
* Start the Jupyter notebook at http://localhost:8888

# 📁 Project Structure
```bash
ai_docker/
├── docker-compose.yml                    # Top-level Compose config
├── model_server/                         # LLaMA model server container
│   ├── app.py                            # Flask app exposing the /generate endpoint
│   ├── Dockerfile                        # Builds the model server container
│   └── requirements.txt                  # All Python dependencies (torch, transformers, etc.)
├── jupyter/                              # Jupyter Notebook environment
│   ├── Dockerfile                        # Builds the Jupyter container
│   └── requirements.txt                  # Jupyter, requests, numpy, pandas, etc.
├── notebooks/                            # Mounted notebook workspace
│   └── llama3_client.ipynb               # Sample notebook to call the model API
```

# ✨ Jupyter Notebook Example
Once running, open notebooks/llama3_client.ipynb and run:

```python
import requests

res = requests.post("http://model:5000/generate", json={
    "prompt": "What is the capital of France?"
})
print(res.json()["response"])
```

# 🔧 Updating Dependencies
Dependencies are managed with Poetry using pyproject.toml files.

To update packages:

```bash
cd jupyter
poetry update

cd ../model_server
poetry update
```
⚠️ poetry.lock is intentionally omitted in this setup. Use poetry lock manually to freeze versions if desired.

# 🧹 Stopping Containers
```bash
docker compose down
```

📬 Questions?
Feel free to open an issue or PR!