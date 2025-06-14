from flask import Flask, jsonify, request
from helper import get_diseases
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return "Hello"
@app.route('/soumil')
def soumil():
    return "Hello! Soumil"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the image file from the request
        file = request.files.get("image_name")
        # print(type(file))
        result,conf = get_diseases(file)
        print("Hello Result:" + result)
        return jsonify({'status': 'Success', 'damage': result,'confidence':str(conf)})
    except Exception as e:
        return jsonify({'status': 'Error', 'message': e})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
