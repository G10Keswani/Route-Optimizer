from flask import Flask, request, jsonify
from optimizer import optimize_route
from utils import get_distance_matrix
import config

app = Flask(__name__)

@app.route('/optimize', methods=['POST'])
def optimize():
    data = request.get_json()
    addresses = data.get('addresses', [])
    if not addresses:
        return jsonify({"error": "No addresses provided"}), 400

    distance_matrix = get_distance_matrix(addresses, config.GOOGLE_MAPS_API_KEY)
    optimized_order = optimize_route(distance_matrix)
    optimized_addresses = [addresses[i] for i in optimized_order]

    return jsonify({"optimized_route": optimized_addresses})

if __name__ == '__main__':
    app.run(debug=True)
