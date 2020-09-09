#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask, request, make_response, render_template, jsonify
import os

app = Flask(__name__)
UPLOAD_DIR = '/nlp-data/uploaded'

@app.route("/")
def home():
    return render_template("text_upload.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5109)
