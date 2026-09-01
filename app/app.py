from flask import Flask, render_template, jsonify
import os
import time
import socket
import platform

app = Flask(__name__)

START_TIME = time.time()


@app.route("/")
def home():
    uptime = int(time.time() - START_TIME)

    days = uptime // 86400
    hours = (uptime % 86400) // 3600
    minutes = (uptime % 3600) // 60
    seconds = uptime % 60

    uptime_text = f"{days}d {hours}h {minutes}m {seconds}s"

    return render_template(
        "index.html",
        hostname=socket.gethostname(),
        platform=platform.system(),
        uptime=uptime_text,
        version="1.0"
    )


@app.route("/health")
def health():

    return jsonify({
        "status": "healthy",
        "application": "DevOps System Monitor",
        "hostname": socket.gethostname()
    })


@app.route("/api/status")
def status():

    return jsonify({
        "application": "DevOps System Monitor",
        "status": "running",
        "hostname": socket.gethostname(),
        "version": "1.0",
        "platform": platform.system()
    })


@app.route("/api/failure")
def failure():

    # Used later to demonstrate monitoring and auto-healing.
    os._exit(1)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
