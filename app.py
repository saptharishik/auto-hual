from flask import Flask,render_template
import firebase_admin
from firebase_admin import credentials,db
cred = credentials.Certificate("database.json")
firebase_admin.initialize_app(cred,{
   "databaseURL": "https://sih1336-default-rtdb.firebaseio.com"})

app = Flask('__main__')

ref = db.reference('/')
data = ref.get()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/V1')
def V1():
    
    altitude = data['v1']['altitude']
    latitude = data['v1']['latitude']
    speed = data['v1']['speed']
    past_pole = data['v1']['past_pol']
    vehicle_id = data['v1']['vehicle_id']
    next_pole = past_pole+1
    vehicle_no = data['v1']['number']

    return render_template('vehicle.html',altitude=altitude,latitude=latitude,vehicle_speed=speed,past_pole=past_pole,vehicle_id=vehicle_id,next_pole=next_pole,vehicle_no=vehicle_no)
@app.route('/V2')
def V2():
    
    altitude = data['v2']['altitude']
    latitude = data['v2']['latitude']
    speed = data['v2']['speed']
    past_pole = data['v2']['past_pol']
    vehicle_id = data['v2']['vehicle_id']
    next_pole = past_pole+1
    vehicle_no = data['v2']['number']

    return render_template('vehicle.html',altitude=altitude,latitude=latitude,vehicle_speed=speed,past_pole=past_pole,vehicle_id=vehicle_id,next_pole=next_pole,vehicle_no=vehicle_no)
@app.route('/V3')
def V3():
    
    altitude = data['v3']['altitude']
    latitude = data['v3']['latitude']
    speed = data['v3']['speed']
    past_pole = data['v3']['past_pol']
    vehicle_id = data['v3']['vehicle_id']
    next_pole = past_pole+1
    vehicle_no = data['v3']['number']

    return render_template('vehicle.html',altitude=altitude,latitude=latitude,vehicle_speed=speed,past_pole=past_pole,vehicle_id=vehicle_id,next_pole=next_pole,vehicle_no=vehicle_no)
@app.route('/V4')
def V4():
    
    altitude = data['v4']['altitude']
    latitude = data['v4']['latitude']
    speed = data['v4']['speed']
    past_pole = data['v4']['past_pol']
    vehicle_id = data['v4']['vehicle_id']
    next_pole = past_pole+1
    vehicle_no = data['v4']['number']

    return render_template('vehicle.html',altitude=altitude,latitude=latitude,vehicle_speed=speed,past_pole=past_pole,vehicle_id=vehicle_id,next_pole=next_pole,vehicle_no=vehicle_no)
app.run(debug=True)