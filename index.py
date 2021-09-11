from firebase import firebase
from flask import Flask , render_template , send_from_directory
import os
import requests

firebase_project_url = os.environ.get('FirebaseProjectUrl')

firebase_app = firebase.FirebaseApplication(firebase_project_url, None)
app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return 'hehe boi'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),  'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():

    result = firebase_app.get('/AlgoDocURL', None)

    abcd = requests.get(result).text
    
    if ('.ngrok.io not found') in abcd or ('Failed to complete tunnel connection' in abcd):
        return render_template('undermaintenance.html')
    else:
        return render_template('hello.html' , algourl = result)

@app.route('/<something>')
def other(something):

    oriurl = firebase_app.get('/AlgoDocURL', None)
    result = oriurl + '/' + something
    
    abcd = requests.get(oriurl).text
    
    if ('.ngrok.io not found' in abcd) or ('Failed to complete tunnel connection' in abcd):
        return render_template('undermaintenance.html')
    else:
        return render_template('hello.html' , algourl = result)
    
@app.route('/v/<some>')
def otherv(some):

    oriurl = firebase_app.get('/AlgoDocURL', None)
    result = oriurl + '/v/' + some
    
    abcd = requests.get(oriurl).text
    
    if ('.ngrok.io not found' in abcd) or ('Failed to complete tunnel connection' in abcd):
        return render_template('undermaintenance.html')
    else:
        return render_template('hello.html' , algourl = result) 

if __name__ == '__main__':
    app.run()
