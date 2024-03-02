from flask import Flask, render_template_string
import folium
import requests
from database import users

app = Flask(__name__)

def convert_Address_To_Coord(person):
    address=person.address
    







@app.route("/")
def display_map_data():
    m=folium.Map(location=(39.683723, -75.749657))
    m.get_root().width = "800px"
    m.get_root().height = "600px"
    iframe = m.get_root()._repr_html_()

    return render_template_string(
        """
            <!DOCTYPE html>
            <html>
                <head></head>
                <body>
                    <h1>People near you with same intrests.</h1>
                    {{ iframe|safe }}
                </body>
            </html>
        """,
        iframe=iframe,
    )
