#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask, request, make_response, render_template, jsonify, redirect, url_for
import os
import json
import tokenizer

app = Flask(__name__)
UPLOAD_DIR = '/nlp-data/uploaded'
TOKENIZE_DIR = '/nlp-data/tokenized'

@app.route("/")
def home():
    return render_template("upload.html")

@app.route("/data/upload", methods=['POST'])
def upload_multipart():
    # TODO: RESTful に変更
    file_ = request.files['uploadFile']
    file_path = os.path.join(UPLOAD_DIR, file_.filename)
    json_filename = '.'.join([file_.filename.split('.')[0], 'json'])
    json_path = os.path.join(TOKENIZE_DIR, json_filename)

    # save uploaded file
    file_.save(file_path)

    # tokenize
    tokenized = tokenizer.tokenize(file_path)
    with open(json_path, 'w') as f:
        json.dump(tokenized, f, ensure_ascii=False, indent=4)

    return redirect(url_for("thanks")) # 関数名で指定

@app.route("/thanks")
def thanks():
    return render_template("thanks.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5108)
