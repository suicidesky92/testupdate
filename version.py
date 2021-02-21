from flask import Flask
app = Flask(__name__)



@app.route('/')
def checker():
    with open('version.txt','r') as file:
        v = file.read()
    return v

@app.route('/newv')
def newv():
    with open('newprog.py','r') as file:
        nv = file.read()
    return nv
