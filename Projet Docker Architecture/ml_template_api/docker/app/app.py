import sys, os
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis-container', port=6379)

#route for home page
@app.route("/")
def hello():
    return "Bienvenue sur mon application  \n\n"


@app.route('/')
def hello():
    redis.incr('hits')
    return ' - - - This basic web page has been viewed {} time(s) - - -'.format(redis.get('hits'))

#route pour accès aux stats
@app.route('/stats')
def stats():
    return 'Accès aux stats'

#@app.route('/tables')
#def tables() -> str:
#    return json.dumps({'Tables ': print_table()})



#run at http://0.0.0.0:5000
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=5000)


