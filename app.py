from flask import Flask, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
from flask import jsonify, render_template, redirect, url_for, flash, send_from_directory, make_response,json
import os

UPLOAD_FOLDER = 'upload_files'

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
CORS(app)


@app.route('/')
def home():
	return render_template('template.html')

# @app.route('/favicon.ico')
# def favicon():
#     # Initialize and load favicon
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                           'favicon.ico', mimetype='image/vnd.microsoft.icon') 

@app.route('/record',methods=['POST'])
def audiovideo():
	if request.method == 'POST':
		file = request.files['audiovideo']
		filename = "myaudiovideo.webm"
		filename = secure_filename(filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	return "success"

if __name__ == "__main__":
	app.run(host="127.0.0.1", debug=False)