from . import web

@web.route('/')
def hello_world():
    return 'Hello World!'