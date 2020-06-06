import time
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def teh_index():
    return render_template("index.html", flask_token="Hello   world")