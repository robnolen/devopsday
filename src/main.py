import os
import redis
import json
import requests
from flask import Flask

app = Flask(__name__)

# default redis config
redis_host = os.getenv('REDIS_HOST')
redis_port = os.getenv('REDIS_PORT')
redis_pw   = os.getenv('REDIS_PW')

#if VCAP_SERVICES is not Nil, then we are in CF, and use rediscloud service
if not os.getenv('VCAP_SERVICES') == None:
    service_data = json.loads(os.getenv('VCAP_SERVICES'))['rediscloud'][0]
    service_creds = service_data['credentials']
    redis_host = service_creds['hostname']
    redis_port = service_creds['port']
    redis_pw   = service_creds['password']

myredis = redis.Redis(host=redis_host, port=redis_port, password=redis_pw)

def get_latest_temps():
    #here we will get and assign the five last temps reported
    foo = "bar"
    return "0"

@app.route('/collect')
def collect():
    #here we will grab input from the photon
    foo = "bar"

@app.route('/')
def index():
    templist = get_latest_temps()
    return """
    <html>
    <head>
        <title>CF Demo App</title>
    </head>
    <body>
        <p align="center">Last five temperature readings from Photon:</p>
        {}<br />
    </body>
    </html>
    """.format(templist)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=int(os.getenv('VCAP_APP_PORT', '5000')))

