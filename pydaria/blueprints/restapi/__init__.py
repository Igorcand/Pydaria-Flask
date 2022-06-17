from flask import Blueprint
from flask_restx import Api

from .resources.product import ProductResource, ProductItemResource
from .resources.product import api as ns1


bp = Blueprint('restapi', __name__, url_prefix='/api/v1')
api = Api(bp, version='1.0',title='Pydaria API',description='A simple pydaria API',doc = '/docs', default_label='Everything about your favorite Pydaria', default = 'Pydaria', license='license')
api.add_namespace(ns1)


def init_app(app):
    api.add_resource(ProductResource, '/product/')
    api.add_resource(ProductItemResource, '/product/<product_id>')
    app.register_blueprint(bp)