from flask import Flask
from yelpApi import request
app = Flask(__name__)

@app.route('/search/<lat>/<lng>')
def search(lat, lng):
    return request(lat, lng)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
