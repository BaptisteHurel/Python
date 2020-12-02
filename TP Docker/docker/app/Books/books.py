
from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from flask import json
import os
from markupsafe import escape
app = Flask(__name__)


@app.route('/')
def renderbook():
    filename = os.path.join(app.json_folder, 'books.json')
    with open(filename) as book_file:
        data = json.load(book_file)
        return jsonify(data)