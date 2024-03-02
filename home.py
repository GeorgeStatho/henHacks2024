from flask import Flask
import requests
app = Flask(__name__)
url="https://us1.locationiq.com/v1/reverse?key=pk.5bc12968439e6e5392783b5b71ad364a&lat=LATITUDE&lon=LONGITUDE&format=json"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
