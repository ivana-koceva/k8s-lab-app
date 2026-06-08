from flask import Flask, jsonify
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

APP_VERSION = "0.1.0"

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(status="ok", version=APP_VERSION)


@app.get("/health")
def health():
    return jsonify(healthy=True)


@app.get("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
