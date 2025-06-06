from flask import Flask, request, jsonify
from llama_cpp import Llama

MODEL_PATH = "/models/TheBloke_deepseek-coder-1.3b-base-GGUF/deepseek-coder-1.3b-base.Q4_K_M.gguf"

app = Flask(__name__)

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=8,
    n_gpu_layers=32
)

PROMPT_TEMPLATE = "<|user|>\n{prompt}\n<|assistant|>\n"

@app.route("/generate", methods=["POST"])
def generate():
    user_prompt = request.json["prompt"]
    prompt = PROMPT_TEMPLATE.format(prompt=user_prompt)
    output = llm(
        prompt,
        max_tokens=128,
        stop=["<|user|>", "<|endoftext|>"],
        echo=False
    )["choices"][0]["text"]
    return jsonify({"response": output.strip()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)