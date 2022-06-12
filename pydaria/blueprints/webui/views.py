from flask import render_template, abort
from models import Product

#def init_app(app):
#    @app.route('/')
def index():
    products = Product.query.all()
    print(products)
    return render_template('index.html',products = products)


    #@app.route('/product/<product_id>')
def product(product_id):
    product = Product.query.filter_by(id=product_id).first() or abort(404, "produto não encontrado")
    return render_template('product.html',product = product)