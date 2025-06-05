from flask import Flask, request, jsonify
from transformers import AutoTokenizer
from awq import AutoAWQForCausalLM
import torch

model_path = "TheBloke/deepseek-coder-1.3b-base-AWQ"

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoAWQForCausalLM.from_pretrained(model_path, trust_remote_code=True)
model = model.to("cuda" if torch.cuda.is_available() else "cpu")
model.eval()

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.json
        prompt = data.get("prompt", "")
        max_new_tokens = int(data.get("max_new_tokens", 256))
        temperature = float(data.get("temperature", 0.7))
        top_p = float(data.get("top_p", 0.95))

        if not prompt:
            return jsonify({"error": "Prompt is required."}), 400

        input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(model.device)

        with torch.no_grad():
            output = model.generate(
                input_ids=input_ids,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                top_p=top_p,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id,
            )

        response_text = tokenizer.decode(output[0], skip_special_tokens=True)
        return jsonify({"response": response_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 