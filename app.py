from flask import Flask,render_template
import firebase_admin
from firebase_admin import credentials,db
import folium
cred = credentials.Certificate("database.json")
firebase_admin.initialize_app(cred,{
   "databaseURL": "https://sih1336-default-rtdb.firebaseio.com"})

app = Flask('__main__')

ref = db.reference('/')
data = ref.get()

def mark_location(latitude, longitude):
    # Create a map centered around the specified location
    location_map = folium.Map(location=[latitude, longitude], zoom_start=15)

    # Add a marker at the specified location
    marker = folium.Marker(location=[latitude, longitude], popup='Marked Location')
    marker.add_to(location_map)

    # Save the map to an HTML file
    location_map.save('templates/map.html')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/V1')
def V1():
    
    longitude = data['v1']['longitude']
    latitude = data['v1']['latitude']
    speed = data['v1']['speed']
    past_pole = data['v1']['past_pol']
    vehicle_id = data['v1']['vehicle_id']
    next_pole = past_pole+1
    vehicle_no = data['v1']['number']
    mark_location(latitude, longitude)
    return render_template('vehicle.html',longitude=longitude,latitude=latitude,vehicle_speed=speed,past_pole=past_pole,vehicle_id=vehicle_id,next_pole=next_pole,vehicle_no=vehicle_no)
@app.route('/V2')
def V2():
    
    longitude = data['v2']['longitude']
    latitude = data['v2']['latitude']
    speed = data['v2']['speed']
    past_pole = data['v2']['past_pol']
    vehicle_id = data['v2']['vehicle_id']
    next_pole = past_pole+1
    vehicle_no = data['v2']['number']
    mark_location(latitude, longitude)

    return render_template('vehicle.html',longitude=longitude,latitude=latitude,vehicle_speed=speed,past_pole=past_pole,vehicle_id=vehicle_id,next_pole=next_pole,vehicle_no=vehicle_no)
@app.route('/V3')
def V3():
    
    longitude = data['v3']['longitude']
    latitude = data['v3']['latitude']
    speed = data['v3']['speed']
    past_pole = data['v3']['past_pol']
    vehicle_id = data['v3']['vehicle_id']
    next_pole = past_pole+1
    vehicle_no = data['v3']['number']
    mark_location(latitude, longitude)

    return render_template('vehicle.html',longitude=longitude,latitude=latitude,vehicle_speed=speed,past_pole=past_pole,vehicle_id=vehicle_id,next_pole=next_pole,vehicle_no=vehicle_no)
@app.route('/V4')
def V4():
    
    longitude = data['v4']['longitude']
    latitude = data['v4']['latitude']
    speed = data['v4']['speed']
    past_pole = data['v4']['past_pol']
    vehicle_id = data['v4']['vehicle_id']
    next_pole = past_pole+1
    vehicle_no = data['v4']['number']
    mark_location(latitude, longitude)

    return render_template('vehicle.html',longitude=longitude,latitude=latitude,vehicle_speed=speed,past_pole=past_pole,vehicle_id=vehicle_id,next_pole=next_pole,vehicle_no=vehicle_no)

@app.route('/map')
def map():
    return render_template("map.html") 
app.run(debug=True)