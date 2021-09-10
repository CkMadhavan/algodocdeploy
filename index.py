from firebase import firebase
from flask import Flask , render_template , send_from_directory
import os
import requests

firebase_project_url = os.environ.get('FirebaseProjectUrl')

firebase_app = firebase.FirebaseApplication(firebase_project_url, None)
app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),  'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():

    result = firebase_app.get('/AlgoDocURL', None)

    if requests.get(result).text.contains('.ngrok.io not found'):
        return 'The server is currently under maintenance , please try again later . We are sorry for the inconvenience caused'
    else:
        return render_template('hello.html' , algourl = result)

@app.route('/<something>')
def other(something):
    result = firebase_app.get('/AlgoDocURL', None) + '/' + something
    return render_template('hello.html' , algourl = result)

if __name__ == '__main__':
    app.run()
