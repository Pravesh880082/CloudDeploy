from flask import Flask, jsonify, render_template
import os
import time

app = Flask(__name__)

START_TIME = time.time()

APP_NAME = os.getenv("APP_NAME", "CloudDeploy")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")


@app.route("/")
def home():
    return render_template(
        "index.html",
        app_name=APP_NAME,
        version=APP_VERSION,
        environment=ENVIRONMENT
    )


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": APP_NAME,
        "version": APP_VERSION
    })


@app.route("/api/status")
def status():
    uptime = round(time.time() - START_TIME, 2)

    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "status": "operational",
        "uptime_seconds": uptime
    })


@app.route("/api/version")
def version():
    return jsonify({
        "version": APP_VERSION
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)