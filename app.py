import numpy as np
from flask import Flask, request, render_template
import pickle
from huggingface_hub import hf_hub_download

app = Flask(__name__)
model = None
scaler = None


@app.before_request
def log_request():
    print(f"Request: {request.method} {request.path}", flush=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return "ok", 200


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
