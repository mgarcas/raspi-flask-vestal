from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data_temp')
def data_temp():
    return render_template('data_temp.html')