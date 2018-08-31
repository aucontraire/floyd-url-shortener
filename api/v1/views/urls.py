#!/usr/bin/python3
'''
    This is our users module.
'''
import models
from models import Url
from api.v1.views import app_views
from flask import jsonify, request, abort, redirect
import string
import random

@app_views.route('/<short_url>')
def do_it(short_url):
    original_url = models.storage.get_url(short_url)
    if original_url is None:
        abort(403)
    return redirect("http://{}".format(original_url.original))

@app_views.route('/create', strict_slashes=False,
                 methods=['POST'])
def create_with_post():
    name_dict = request.get_json()
    try:
        original_url = name_dict['original']
    except KeyError:
        abort(404)
    short_url = Url()
    setattr(short_url, "original", original_url)
    setattr(short_url, "short_url", hashfunc())
    models.storage.new(short_url)
    models.storage.save()
    return jsonify(short_url.to_dict())

@app_views.route('/create/<original_url>', strict_slashes=False,
                 methods=['GET'])
def make_it(original_url):
    short_url = Url()
    setattr(short_url, "original", original_url)
    setattr(short_url, "short_url", hashfunc())
    models.storage.new(short_url)
    models.storage.save()
    return jsonify(short_url.to_dict())

@app_views.route('/delete/<original>')
def destroy_it():
    result = storage.delete(original)
    if result is None:
        return "{} didn't exist".format(original), 403
    return "Deleted"

def hashfunc():
    return(''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
