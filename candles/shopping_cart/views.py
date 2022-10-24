from flask import session, Blueprint, redirect, url_for
from candles.products.models import Product

bp = Blueprint('shopping_cart', __name__)


@bp.route('/add_product/<product_id>/', methods=['GET', 'POST'])
def add_product(product_id):

    if 'shopping_cart' not in session:
        session['shopping_cart'] = {}

    if product_id in session['shopping_cart']:
        session['shopping_cart'][product_id] += 1
    else:
        session['shopping_cart'][product_id] = 1

    session.modified = True

    return redirect(url_for('index'))


@bp.route('/clear_cart/', methods=['GET', 'POST'])
def clear_cart():
    session.pop('shopping_cart')
    return redirect(url_for('index'))


@bp.route('/delete_product/<product_id>/', methods=['GET', 'POST'])
def delete_product(product_id):
    if 'shopping_cart' in session:
        if product_id in session['shopping_cart']:
            if session['shopping_cart'][product_id] > 1:
                session['shopping_cart'][product_id] -= 1
            else:
                session['shopping_cart'].pop(product_id)

            session.modified = True

    return redirect(url_for('index'))
