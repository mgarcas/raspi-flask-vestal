from app import app

if __name__ == '__main__':
    # app.run(host='192.168.0.7', port=5000, debug=True)
    # app.run()
    app.run(host='0.0.0.0', port=8080, debug=True)

