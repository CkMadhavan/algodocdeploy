from firebase import firebase
from flask import Flask , render_template
import os

firebase_project_url = os.environ.get('FirebaseProjectUrl')

firebase_app = firebase.FirebaseApplication(firebase_project_url, None)
app = Flask(__name__)

result = firebase_app.get('/AlgoDocURL', None)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),  'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('hello.html' , algourl = result)

@app.route('/<something>')
def other(something):
    result = result + '/' + something
    return render_template('hello.html' , algourl = result)

if __name__ == '__main__':
    app.run()
