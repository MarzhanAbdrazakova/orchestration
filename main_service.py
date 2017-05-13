from flask import Flask
from flask import request
import json
import requests
app = Flask(__name__)

@app.route('/', methods=['POST'])
def api():
    data=request.get_data()
    resp=json.loads(data)
    i=2
    d={int(k): (v) for k,v in resp.items()}
    if d[1]=="+":
        url='http://10.0.0.2:5000'
    elif d[1]=="*":
        url='http://10.0.0.2:5300'
    elif d[1]=="/":
        url='http://10.0.0.2:5200'
    elif d[1]=="-":
        url='http://10.0.0.2:5100'
    p=requests.post(url,json.dumps(d))
    q=json.dumps(p.json())
    r=json.loads(q)
    while i <= (len(d.keys())-2):
        if r["1"]=="+":
            url='http://10.0.0.2:5000'
        elif r["1"]=="*":
            url='http://10.0.0.2:5300'
        elif r["1"]=="/":
            url='http://10.0.0.2:5200'
        elif r["1"]=="-":
            url='http://10.0.0.2:5100'
        p=requests.post(url,json.dumps(r))
        q=json.dumps(p.json())
        r=json.loads(q)
        i+=2
    return p.text
if __name__ == '__main__':
    app.run(host='10.0.0.2',port=4900)
