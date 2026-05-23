from flask import Flask, jsonify
import time

app = Flask(__name__)
counts = {"time_calls": 0}

@app.route('/time')
def get_time():
    counts["time_calls"] += 1
    return jsonify({"time": int(time.time())})

@app.route('/metrics')
def get_metrics():
    return jsonify({"count": counts["time_calls"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
