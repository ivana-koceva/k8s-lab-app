from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

APP_VERSION = "0.1.0"

app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info("app_info", "Application info", version=APP_VERSION)


@app.get("/")
def index():
    return jsonify(status="ok", version=APP_VERSION)


@app.get("/health")
def health():
    return jsonify(healthy=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)