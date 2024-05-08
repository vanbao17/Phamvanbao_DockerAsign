import os
import sys
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
import json as js
import logging
import schedule
import time
app = Flask(__name__)
CORS(app)
from api import fetch_books
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', stream=sys.stdout)
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_dir)
logger = logging.getLogger(__name__)
@app.route('/crawl', methods=['GET'])
def crawl():
    logger.debug("đang chạy")
    try:
        books = fetch_books()
        logger.debug(f"Found data:{books}")
    except:
        logger.error("Error fetching books data: {}".format(e))
        return jsonify({"error": "du lieu fetch sai roi"}), 500
    
    try:
        response = requests.post('http://mysql_api_container:5000/insert',json=books)
    except:
        return jsonify({"error": "khong ket noi duo vowi db"}), 500
    try:
        if response.status_code == 200:
            return jsonify({"message": "Data inserted successfully","data":books}), 200
        else:
            return jsonify({"error": "Failed to insert data: " }), 500
    except Exception as e:
        return jsonify({"error": "An error occurred during data insertion"}), 500

schedule.every().day.at("02:35").do(crawl)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
