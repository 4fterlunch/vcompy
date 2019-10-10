from flask import Flask, jsonify, request, render_template, escape
import sys, os
import json
from subprocess import Popen, PIPE, TimeoutExpired
import threading, logging

app= Flask(__name__)

readings=[]


def start_listener():
    sensor = Popen(['python', 'obd_sensors.py'], stdout=PIPE)
    buffer=b''
    while listener_thread.isAlive:
        char = sensor.stdout.read(1)
        
        if buffer.endswith(b'/') and char == b'n':
            readings.append(buffer[:-1].decode())
            buffer=b''
        else:
            buffer+=char
           
        

listener_thread = threading.Thread(target=start_listener, daemon=True)
listener_thread.start()




@app.route('/')
def run_vcompy():
    global listener_thread

    
    return render_template('vcompy.html',message="vCOMpy v1.0")



@app.route('/sensor/<name>')
def hello(name):
    return '%s' % name

@app.route('/sensors',methods=['GET'])
def resolveSensorRequest():
    # if request.method == 'POST':
    #     print('POST message received')
    #     print(request.get_json())
    #     return 'OK', 200
    # else:
    #     print('returning data for GET')
    #     message = {"from": __name__}
    return readings[len(readings)-1]