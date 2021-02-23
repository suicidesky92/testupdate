import dbconnm
from flask import Flask, request
from datetime import datetime


app = Flask(__name__)

MONGO_HOST='localhost'

client = dbconnm.pymongo.MongoClient(MONGO_HOST, 27017)
db = client['TestDB']
#coll = db['TestC']

needkeys = set(("Electric","Water","Gas"))

@app.route('/getv')
def checker():
    with open('./version.txt','r') as file:
        v = file.read()
    return v

@app.route('/newv')
def newv():
    with open('./client/prog.py','r') as file:
        nv = file.read()
    return nv

@app.route('/add/<coll>', methods=['POST'])
def add(coll):
    coll = db[coll]
    headers = dict(request.headers)
    data = dict((k,v) for k,v in headers.items() if k in needkeys)
    data |= dict(Date=gettime())
    nowtime = str(gettime())
    print(str(coll))
    if dbconnm.find_document(coll, dict(Date=nowtime)) != None and str(gettime()) in dict(dbconnm.find_document(coll, dict(Date=nowtime))).values(): dbconnm.delete_document(coll, dict(Date=nowtime))
    return str(dbconnm.insert_document(coll, data))

@app.route('/find/<coll>', methods=['GET'])
def find(coll):
    coll = db[coll]
    headers = dict(request.headers)
    data = dict((k,v) for k,v in headers.items() if k in needkeys)
    resp = dict(dbconnm.find_document(coll, data))
    _ = resp.pop('_id')
    return resp

@app.route('/update/<coll>', methods=['POST'])
def update(coll):
    coll = db[coll]
    return dbconnm.update_document(coll, data)

@app.route('/delete/<coll>', methods=['DELETE'])
def delete(coll):
    coll = db[coll]
    return dbconnm.delete_document(coll, data)

@app.route('/test/<test>', methods=['GET', 'POST'])
def test(test):
    method = request.method
    headers = dict(request.headers)
    print(f'{method} --- {headers}')
    return f'{method} --- {headers}'


def gettime():
    now = datetime.now()
    return now.strftime('%Y-%m-%d')



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
