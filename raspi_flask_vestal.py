from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data_temp')
def data_temp():
    return render_template('data_temp.html')


if __name__ == '__main__':
    app.run(host='192.168.0.7', port=5000, debug=True)
