# hello world
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

@app.route('login')
def login():
    return 'login success'

if __name__=='__main__':
    app.run(debug=True)
