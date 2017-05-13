from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def api():
    data=request.get_data()
    resp=json.loads(data)
    url='http://10.0.0.2:4900'
    d={int(k): (v) for k,v in resp.items()}
    res=int(d[0])/int(d[2])
    d[0]=res
    m=3
    if len(d.keys())==3: 
        return (json.dumps(res))
    for i in range(1,len(d.keys())-2):
        d[i]=d.pop(m)
        i+=1
        m+=1
    return (json.dumps(d))

if __name__ == '__main__':
    app.run(host='10.0.0.2',port=5200)

