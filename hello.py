from flask import Flask

app = Flask(__name__)

   
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.logger.debug('A value for debugging')
@app.logger.warning('A warning occurred (%d apples)', 42)
@app.logger.error('An error occurred')