#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask, request, make_response, render_template, jsonify, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_DIR = '/nlp-data/uploaded'

@app.route("/")
def home():
    return render_template("upload.html")

@app.route("/data/upload", methods=['POST'])
def upload_multipart():
    # TODO: RESTful に変更
    file_ = request.files['uploadFile']
    fileName = file_.filename

    file_.save(os.path.join(UPLOAD_DIR, fileName))
    return redirect(url_for("thanks")) # 関数名で指定

@app.route("/thanks")
def thanks():
    return render_template("thanks.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5108)
