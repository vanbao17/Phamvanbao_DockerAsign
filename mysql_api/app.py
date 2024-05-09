from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os


project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_dir)


from data import search_books, get_books, save_to_db

app = Flask(__name__)
CORS(app)
@app.route('/insert', methods=['POST'])
def insert_data():
    data = request.get_json()
    try:
        save_to_db(data)
        return jsonify({"message": "Data inserted successfully"}), 200
    except Exception as e:
        return jsonify({"error"}), 500

@app.route('/books', methods=['GET'])
def get_data():
    try:
        books = get_books()
        return jsonify({
            "message": "Get data successfully",
            "data": books
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/search', methods=['POST'])
def search_data():
    data = request.get_json()
    if 'query' not in data:
        return jsonify({"error": "Query parameter is missing"}), 400  # Kiểm tra dữ liệu đầu vào
    try:
        books = search_books(data['query'])
        return jsonify({
            "message": "Get data successfully",
            "data": books
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
