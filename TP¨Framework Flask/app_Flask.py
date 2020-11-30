from flask import Flask
app = Flask(__name__)

#route principale
@app.route("/")
def index():
 return "Première app avec framework Flask"
if __name__ == '__main__':
    app.run(debug=True)

           
           
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'