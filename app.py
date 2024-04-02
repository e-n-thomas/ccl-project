from flask import Flask, render_template, request, send_file
from helper import delete_files, convert
import os

app = Flask(__name__)


@app.route('/')
def index():
    delete_files("files/")
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_file():
    file = request.files['file']
    format = request.form['conversion_format']
    file.save('files/' + file.filename)
    convert("files/"+file.filename,format)
    return send_file(os.getcwd()+"/files/"+file.filename.split('.')[0]+"."+format,as_attachment=True)


if __name__ == '__main__':
    app.run(debug=False)
