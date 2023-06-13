from flask import render_template, request
from app import app
from pi import pi_functions
from database import Tempsys

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/temp', methods=['POST','GET'])
def temp():
    if request.method == 'POST':
        result = pi_functions.getTemp()
        return render_template('temp.html', result=result)
    else:
        return render_template('temp.html')


@app.route('/data_temp')
def data_temp():
    return render_template('data_temp.html')


@app.route('/data')
def data():
    # Retrieve all data from the "tempsys" table
    all_data = Tempsys.query.all()

    # Pass the data to the template
    return render_template('data.html', data=all_data)