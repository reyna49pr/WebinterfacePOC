from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/control', methods=['POST'])
def control():
    data = request.json
    device = data.get("device")
    action = data.get("action")
    if not device or not action:
        return jsonify({"error": "Device and action must be specified."})
    # Mock response for demonstration purposes
    return jsonify({"message": f"{action.capitalize()} command sent to {device.capitalize()}."})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
