import os
import sys
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
import json as js
import logging
app = Flask(__name__)
CORS(app)

# Giả sử rằng 'api' là một module bạn tự định nghĩa chứa hàm fetch_books
from api import fetch_books

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_dir)

@app.route('/crawl', methods=['GET'])
def crawl_data():
    try:
        books = fetch_books()
        logging.debug(f"Found data:{books}")
    except:
        return jsonify({"error": "du lieu fetch sai roi"}), 500
    
    try:
        response = requests.post('http://mysql_api_container:5000/insert',json=books)
    except:
        return jsonify({"error": "khong ket noi duo vowi db"}), 500
    try:
        if response.status_code == 200:
            return jsonify({"message": "Data inserted successfully"}), 200
        else:
            return jsonify({"error": "Failed to insert data: " }), 500
    except Exception as e:
        return jsonify({"error": "An error occurred during data insertion"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
