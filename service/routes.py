"""Routes for the counter service."""
from flask import jsonify
from service import app

COUNTERS = {}


@app.route("/")
def index():
    """Return service info."""
    return jsonify(name="Counter Service", version="1.0"), 200


@app.route("/health")
def health():
    """Health check endpoint."""
    return jsonify(status="OK"), 200


@app.route("/counters/<name>", methods=["POST"])
def create_counter(name):
    """Create a counter starting at zero."""
    if name in COUNTERS:
        return jsonify(error=f"Counter {name} already exists"), 409
    COUNTERS[name] = 0
    return jsonify(name=name, counter=0), 201


@app.route("/counters/<name>", methods=["PUT"])
def update_counter(name):
    """Increment a counter."""
    if name not in COUNTERS:
        return jsonify(error=f"Counter {name} not found"), 404
    COUNTERS[name] += 1
    return jsonify(name=name, counter=COUNTERS[name]), 200


@app.route("/counters/<name>", methods=["GET"])
def read_counter(name):
    """Read a counter."""
    if name not in COUNTERS:
        return jsonify(error=f"Counter {name} not found"), 404
    return jsonify(name=name, counter=COUNTERS[name]), 200
