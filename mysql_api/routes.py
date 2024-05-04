from app import app, mysql
from flask import request, jsonify
from src.data import save_to_db,get_books,search_books
import sys
import os
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_dir)
@app.route('/insert', methods=[ 'POST'])
def insert_data():
    # Lấy dữ liệu từ JSON request
    data = request.get_json()
    try:
        save_to_db(data)
        return jsonify({"message": "Data inserted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/books', methods=['GET'])
def get_data():
    try:
        books=get_books()
        return jsonify({
            "message": "Get data successfully",
            "data":books
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/search', methods=['POST'])
def search_data():
    data = request.get_json()
    try:
        books=search_books(data['query'])
        return jsonify({
            "message": "Get data successfully",
            "data":books
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


    