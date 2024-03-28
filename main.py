import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

#loading Dataset
cleaned_data = pd.read_csv('cleaned_task_data.csv')

# GET request for fetching all records
@app.route('/records', methods=['GET'])
def get_all_records():
    return jsonify(cleaned_data.to_dict(orient='records'))

# Filter Endpoint
@app.route('/filter', methods=['POST'])
def filter_records():
    req_data = request.get_json()
    min_price = req_data.get('min_price', 0)
    max_price = req_data.get('max_price', float('inf'))
    filtered_data = cleaned_data[(cleaned_data['price'] >= min_price) & (cleaned_data['price'] <= max_price)]
    return jsonify(filtered_data.to_dict(orient='records'))

# Endpoint to insert new records into the dataset (POST request).
@app.route('/insert', methods=['POST'])
def insert_record():
    req_data = request.get_json()
    cleaned_data = cleaned_data.append(req_data, ignore_index=True)
    return jsonify({"message": "Record inserted successfully."})

if __name__ == '__main__':
    app.run(debug=True)
