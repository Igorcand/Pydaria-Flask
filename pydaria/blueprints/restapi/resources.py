from flask import abort, jsonify
from flask_restful import Resource

from models.product import Product


class ProductResource(Resource):
    def get(self):
        products = Product.query.all() or abort(204)
        print(products)
        return jsonify(
            {"products": [x.json() for x in products]}
        )


class ProductItemResource(Resource):
    def get(self, product_id):
        product = Product.query.filter_by(id=product_id).first() or abort(404)
        return jsonify(product.json())