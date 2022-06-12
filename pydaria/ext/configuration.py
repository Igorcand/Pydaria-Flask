from importlib import import_module

from dynaconf import FlaskDynaconf


def load_extensions(app):
    for extension in app.config.get('EXTENSIONS'):
        # Split data in form `extension.path:factory_function`
        mod = import_module(extension)
        # Dynamically import extension module.
        mod.init_app(app)
        # Invoke factory passing app.
        


def init_app(app, **config):
    FlaskDynaconf(app, **config)