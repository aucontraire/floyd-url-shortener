#!/usr/bin/python3
'''
    This module contains the routes for the visitor service
'''
from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
from api.v1.views import app_views

import models
from models import Url


app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views, url_prefix="/api/v1")
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

@app.route('/')
def status():
    return jsonify({"status": "ok"})

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == "__main__":
    app.run(port=5003)
