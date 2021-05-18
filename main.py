import flask
from flask_cors import CORS
from flask import Flask
from main_hw import app_hw

app = Flask(__name__)
app.register_blueprint(app_hw)
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app)

@app.route('/')
def index():
    return flask.send_from_directory('demo', 'production/index.html')

@app.route('/favicon.ico') 
def favicon(): 
    return flask.send_from_directory('demo', 'production/loveheart.ico', mimetype='image/vnd.microsoft.icon')

app.run(host='0.0.0.0', port=11666, debug=True)
