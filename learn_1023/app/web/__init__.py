from flask import Flask, jsonify,Blueprint
web = Blueprint('web',__name__)

from app.web import book,hello_world