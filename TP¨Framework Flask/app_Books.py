from flask import Flask
app = Flask(__name__)

from flask import render_template


import json

#url = http://127.0.0.1:5000/

#route principale
@app.route("/")
def index():
 return "hello my app"
if __name__ == '__main__':
    app.run(debug=True)

    
#variable book
book=[
	{
		'id':1,
		'titre' : 'un titre',
	},
	{
		'id':2,
		'titre': 'un autre titre random',
	}
]
    
#url = http://127.0.0.1:5000/api/books   
@app.route('/api/books', methods=["GET"])
def index():
    response = get_a_response()
    return response


