from flask import Flask

def create_app(config=None):
    app = Flask(__name__)
    register_blueprint(app)
    return app

def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
