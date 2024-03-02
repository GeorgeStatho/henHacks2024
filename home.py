from flask import Flask
import requests
app = Flask(__name__)
url = "https://us1.locationiq.com/v1/reverse"
data = {
        'key': 'pk.5bc12968439e6e5392783b5b71ad364a',
        'lat': '-37.870662',
        'lon': '144.9803321',
        'format': 'json'
    }
response = requests.get(url, params=data)
print(response.text)
@app.route("/")
def map_data():
    return response.text

