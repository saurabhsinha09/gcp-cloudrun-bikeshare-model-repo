import pandas as pd
from flask import Flask, request, jsonify
import joblib
import os
from google.cloud import storage

app = Flask(__name__)
model = None

#Local model testing
def load_model():
    model = joblib.load("randomforest_bikesharing_model.joblib")
    return model

#Testing from cloud model.
def load_model_cloud():
    storage_client = storage.Client()
    bucket_name = "dcn-aiml-vertexai-mlops"
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob("models/randomforest_bikesharing_model.joblib")
    blob.download_to_filename("randomforest_bikesharing_model.joblib")
    model = joblib.load("randomforest_bikesharing_model.joblib")
    return model

@app.route('/predict', methods=['POST'])
def predict():
    # Uncomment this while running from local system 
    #model = load_model()
    
    # Uncomment this while running from cloud
    model = load_model_cloud()
    try : 
        input_json = request.get_json()
        input_df = pd.DataFrame(input_json, index=[0])
        y_predictions = model.predict(input_df)
        response = {'predictions': y_predictions.tolist()}
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5052)))
