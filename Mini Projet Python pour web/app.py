from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Bienvenue sur ma web app Python'