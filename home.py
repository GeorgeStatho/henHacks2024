from flask import Flask, render_template_string, render_template, request
import folium
import requests
from database import users
from database import Person
import math

app = Flask(__name__)

def convert_Address_To_Coord(person:Person):
    #Assuming Adresses will be with Street name and number, town, state, zipcode, in that order
    #Note: Street Number and name assumed to have no space inbetween them.
    address=person.Address.split()
    url = "https://us1.locationiq.com/v1/search/structured?key=pk.5bc12968439e6e5392783b5b71ad364a"
    for i in range(len(address)-1):
        if(i<len(address)-1):
            url+=address[i]+"%20"
        else:
            url+=address[i]+"&format=json&"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers).json()
    lat=response["lat"]
    lon=response["lon"]
    return lat,lon


def get_distance(lat1, lat2, lon1, lon2):
    distkm = math.acos(math.sin(lat1)*math.sin(lat2)+math.cos(lat1)*math.cos(lat2)*math.cos(lon2-lon1))*6371
    distmile = distkm / 1.609
    return distmile

def place_marker(target:Person,people:list,max_distance:int,map):
    target_lat,target_lon=convert_Address_To_Coord(target)
    for person in people:
        person_lat,person_lon=convert_Address_To_Coord(person)
        if(get_distance(target_lat,target_lon,person_lat,person_lon)<max_distance and target.Interest==person.Interest):
            folium.Marker(location=[person_lat,person_lon],name=person.name).add_to(map)

@app.route("/")
def display_map_data():
    m=folium.Map(location=(39.683723, -75.749657))
    place_marker(users[-1],users,5,m)
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
