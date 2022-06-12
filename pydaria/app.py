from flask import Flask
from ext import configuration


def create_app():
    app = Flask(__name__)

    configuration.init_app(app)
    #app = minimal_app()
    configuration. load_extensions(app)
    return app


def minimal_app():
    app = Flask(__name__)

    configuration.init_app(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)