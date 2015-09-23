import os
import redis
import json
import datetime
from flask import Flask, render_template, request
from kairos import Timeseries

app = Flask(__name__)


# default redis config
redis_host = os.getenv('REDIS_HOST')
redis_port = os.getenv('REDIS_PORT')
redis_pw   = os.getenv('REDIS_PW')

#if VCAP_SERVICES is not Nil, then we are in CF, and use rediscloud service
if not os.getenv('VCAP_SERVICES') == None:
    service_data = json.loads(os.getenv('VCAP_SERVICES'))['redis'][0]
    service_creds = service_data['credentials']
    redis_host = service_creds['host']
    redis_port = service_creds['port']
    redis_pw   = service_creds['password']

myredis = redis.Redis(host=redis_host, port=redis_port, password=redis_pw)
ts = Timeseries(myredis, type='series', intervals={
    'second': {
        'step' : 1,
        'steps' : 20400,
    }
})

@app.template_filter()
def convert_timestamp(ts):
    stamp = datetime.datetime.fromtimestamp(ts)
    return stamp.strftime('%Y-%m-%d %H:%M:%S')

app.jinja_env.filters['tsfilter'] = convert_timestamp

def get_latest_temps():
    #here we will get and assign the temps reported
    series = ts.series('temp', 'second')
    for x in series.items():
        if not x[1]:
            series.pop(x[0])
    return series

@app.route('/collect', methods=['POST'])
def collect():
    #here we will grab input from the photon
    temperature = 0
    timestamp = 0
    if request.method == 'POST':
        temperature = request.form['temp']
    
    ts.insert('temp', temperature)
    foo = ts.series('temp', 'second')
    return "{}".format(foo)

@app.route('/')
def index():
    templist = get_latest_temps()
    return render_template('default.html', temps=templist)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=int(os.getenv('VCAP_APP_PORT', '5000')))

