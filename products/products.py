from flask import Blueprint, render_template
#from ecommerce.models import Product

products_bp = Blueprint('products_bp', __name__,
    template_folder='templates',
    static_folder='static', 
    static_url_path='assets')

@products_bp.route('/')
def list():
    products = [
        {
            'rasm': 'Pomidor',
            'nom': 'Pomidor',
            'narx': 100000,
            'yaroqlilik': 30
        },
        {
            'rasm': 'Bodiring',
            'nom': 'Bodiring',
            'narx': 100000,
            'yaroqlilik': 30
        },
        {
            'rasm': 'Kartoshka',
            'nom': 'Kartoshka',
            'narx': 100000,
            'yaroqlilik': 90
        },
        {
            'rasm': 'Piyoz',
            'nom': 'Piyoz',
            'narx': 100000,
            'yaroqlilik': 100
        }
    ]
    return render_template('products/list.html', products=products)

# @products_bp.route('/view/<int:product_id>')
# def view(product_id):
#     product = Product.query.get(product_id)
#     return render_template('products/view.html', product=product)