
from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/weatherapp', methods=['POST', "GET"])
def get_weather_data():
    url = 'https://api.openweathermap.org/data/2.5/weather'

    param = {
        'q': request.form.get("city"),
        'units': 'metric',
        'appid': '3b523e09df73ca1a0d26a8e4ce8d7f17'
    }

    response = requests.get(url, params=param)
    data = response.json()
    city = data['name']
    return render_template('response.html', data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
