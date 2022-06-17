from flask import abort, jsonify
from flask_restx import Resource, Namespace, fields

from models.product import Product

api = Namespace(name='products', description='Products related operations')

product_doc = api.model('Product', 
{
    'id':fields.Integer(description='O id do produto'),
    'name': fields.String(required=True, min_lenght=1, max_lenght=30, description='O nome do produto'),
    'price':fields.Integer(description='O preço do produto'),
    'description':fields.String(description='A descrição do produto'),
})


class ProductResource(Resource):
    @api.doc('list_product')
    @api.marshal_with(product_doc)
    def get(self):
        prod = Product.query.all() 
        return [Product(id=x.id, name=x.name, price=x.price, description=x.description).json() for x in prod]  


@api.param('id', 'The product identifier')
@api.response(404, 'Product not found')
class ProductItemResource(Resource):
    @api.doc('get_product')
    @api.marshal_with(product_doc)
    def get(self, product_id):
        product = Product.query.filter_by(id=product_id).first() or api.abort(404)
        return Product(id=product.id, name=product.name, price=product.price, description=product.description)