# setting up a flask api

from flask import Flask, request, jsonify
import pickle
import numpy as np

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.get('/')
def index():
    return "Welcome to the deploy a model code"

@app.post('/predict')
def predict():
    data = request.json
    features = np.array(data['features']).reshape(1, -1)
    
    prediction = model.predict(features)
    return jsonify({
        "features": str(prediction[0])
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)