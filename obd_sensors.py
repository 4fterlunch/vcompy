import random, time, json
import obd

while True:
    time.sleep(1)  # wait 0 to 5 seconds
    temperature = (random.randrange(start=-5, stop=200))
    rpm = (random.randrange(start=900, stop=6000, step=100))
    speed = (random.randrange(start=0, stop=100, step=5))
    ambient_temperature = (random.randrange(start=18, stop=22))
    sensors = {
        "engine" : {
            "temperature": temperature,
            "rpm": rpm,
            "speed":speed
        },
        "environment" : {
            "ambient_temperature" : ambient_temperature
        }
        
    }
    print(json.dumps(sensors), flush=True, end='/n')