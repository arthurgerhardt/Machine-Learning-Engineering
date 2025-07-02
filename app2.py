from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flasgger import Swagger

auth = HTTPBasicAuth()

app = Flask(__name__)

app.config['SWAGGER'] = {
    'title': 'API de Exemplo',
    'version': '1.0.0',
    'uiversion': 3
    
}

swagger = Swagger(app)

