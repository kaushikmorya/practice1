from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()

# MongoDB connection
client = MongoClient(os.getenv("MONGO_URI"))
db = client['your_database_name']
collection = db['your_collection_name']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    data = list(collection.find({}, {'_id': 0}))
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def add_data():
    new_data = request.json
    collection.insert_one(new_data)
    return jsonify({'message': 'Data added successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
