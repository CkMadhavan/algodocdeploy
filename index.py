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

    if '.ngrok.io not found' in requests.get(result).text:
        return 'The server is currently under maintenance , please try again later . We are sorry for the inconvenience caused'
    else:
        return render_template('hello.html' , algourl = result)

@app.route('/<something>')
def other(something):

    oriurl = firebase_app.get('/AlgoDocURL', None)
    result = oriurl + '/' + something
    
    if '.ngrok.io not found' in requests.get(oriurl).text:
        return 'The server is currently under maintenance , please try again later . We are sorry for the inconvenience caused'
    else:
        return render_template('hello.html' , algourl = result)

if __name__ == '__main__':
    app.run()
