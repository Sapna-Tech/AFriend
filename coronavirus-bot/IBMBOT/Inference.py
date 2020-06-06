
from flask import Flask, request, jsonify, make_response
import os
import json
from flask_api import status
from flask_basicauth import BasicAuth

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from pathlib import Path

from IBMBOT.utils import ConfigLoading
from IBMBOT.InferenceService import InferenceService

app = Flask(__name__)

port = int(os.getenv('PORT', 8000))

InferenceService = InferenceService()

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = Path(DIR_PATH).parents[0]
CONFIG_FILE = os.path.join(ROOT_DIR, 'config/config.json')
config = json.load(open(CONFIG_FILE))

app.config['BASIC_AUTH_USERNAME'] = config['BASIC_AUTH_USERNAME']
app.config['BASIC_AUTH_PASSWORD'] = config['BASIC_AUTH_PASSWORD']
basic_auth = BasicAuth(app)

loading_ = ConfigLoading(config['model'][0])


@app.route('/')
def root():
    return make_response(
        '{"status": 200, "description": "ML server rejects your request"}')


@app.route('/api/predict', methods=['GET'])
@basic_auth.required
def predict():

    if 'text' not in request.args:
        resp_text = make_response(
            '{"status":400,"description":"No text received."}')
        return resp_text, status.HTTP_400_BAD_REQUEST

    if 'ani' not in request.args:
        resp_ani = make_response(
            '{"status":400,"description":"No ani received."}')
        return resp_ani, status.HTTP_400_BAD_REQUEST

    text = request.args.get('text')
    ani = request.args.get('ani')

    result, url = InferenceService.inference(text, ani, loading_)
    if not result and not url:
        result = InferenceService.randomize(loading_.default_response)
    response = {"response": result, "url": url}

    return jsonify(response)


if __name__ == '__main__':
    http_server = HTTPServer(WSGIContainer(app))
    http_server.bind(port)
    http_server.start(0)
    IOLoop.current().start()
