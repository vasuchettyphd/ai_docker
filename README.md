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
.
├── docker-compose.yml
├── jupyter/
│   ├── Dockerfile
│   └── pyproject.toml
├── model_server/
│   ├── Dockerfile
│   ├── pyproject.toml
│   └── app.py
└── notebooks/
    └── llama3_client.ipynb
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