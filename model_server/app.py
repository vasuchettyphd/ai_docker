from awq import AutoAWQForCausalLM
from transformers import AutoTokenizer
from flask import Flask, request, jsonify

app = Flask(__name__)

model_path = "TheBloke/deepseek-coder-1.3b-base-AWQ"
model = AutoAWQForCausalLM.from_quantized(
    model_path,
    fuse_layers=True,
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Missing 'prompt' in request body"}), 400

    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.cuda()
    with torch.no_grad():
        output_ids = model.generate(input_ids, max_new_tokens=256)
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return jsonify({"output": output_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)