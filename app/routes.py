from flask import render_template, request
from app import app, db
from pi import pi_functions
from database import Tempsys


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pi/temp', methods=['POST', 'GET'])
def temp():
    if request.method == 'POST':
        result = pi_functions.getTemp()
        return render_template('temp.html', result=result)
    else:
        last_data = db.session.execute(db.select(Tempsys).filter_by(id='20230608')).scalar_one()
        all_data = db.session.execute(db.select(Tempsys).order_by(Tempsys.id)).scalars()
        print(last_data)
        print(all_data.all())
        return render_template('temp.html')


# @app.route('/pi/data_temp')
# def data_temp():
#     return render_template('data_temp.html')


@app.route('/pi/data_temp')
def data_temp():
    # Retrieve all data from the "tempsys" table
    all_data = Tempsys.query.all()

    # Pass the data to the template
    return render_template('data_temp.html', data=all_data)


@app.route('/pi/camera')
def picamera():
    return render_template('picamera.html')
