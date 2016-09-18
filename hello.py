from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/add/<int:a>/<int:b>')
def add_ab(a,b):
    # a+b
    return '%d + %d = %d' % (a,b,a+b)