import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(
        message="Hello from ECS Fargate",
        version=os.environ.get("APP_VERSION", "dev"),
    )


@app.get("/health")
def health():
    return jsonify(status="ok"), 200
