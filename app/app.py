from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Connect to Redis
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def home():
    return jsonify({
        'message': 'Flask app is running!',
        'status': 'ok'
    })

@app.route('/test')
def test():
    # Increment a counter in Redis
    count = redis_client.incr('test_counter')
    return jsonify({
        'endpoint': 'test',
        'visits': count,
        'status': 'ok'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
