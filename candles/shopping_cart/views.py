from flask import session, Blueprint, redirect, url_for, request, render_template, jsonify
from candles.content.models import Product
from candles.feedback.forms import BasketForm

bp = Blueprint('shopping_cart', __name__)


def set_total_price():

    products = Product.objects(id__in=session['shopping_cart'].keys())
    if products:
        total = 0
        for product in products:
            total += product.price * session['shopping_cart'][str(product.id)]

        session['shopping_cart_total'] = total


@bp.route('/add_product/<product_id>/', methods=['GET', 'POST'])
def add_product(product_id):

    if 'shopping_cart' not in session:
        session['shopping_cart'] = {}

    if product_id in session['shopping_cart']:
        session['shopping_cart'][product_id] += 1
    else:
        session['shopping_cart'][product_id] = 1

    set_total_price()

    session.modified = True

    # ajax logic
    request_xhr_key = request.headers.get('X-Requested-With')
    if request_xhr_key and request_xhr_key == 'XMLHttpRequest':

        catalog_btn_template = render_template('includes/catalog_btn_template.html', product_id=product_id)
        basket_info = render_template(
            'includes/basket.html',
            product_id=product_id,
            basket_products=Product.objects(id__in=session['shopping_cart'].keys()),
            basket_form=BasketForm(),
        )
        context = {
            'catalog_btn_template': catalog_btn_template,
            'basket_info': basket_info
        }
        return jsonify(context)

    return redirect(url_for('index'))


@bp.route('/clear_cart/', methods=['GET', 'POST'])
def clear_cart():
    try:
        session.pop('shopping_cart')
    except:
        pass

    # ajax logic
    request_xhr_key = request.headers.get('X-Requested-With')
    if request_xhr_key and request_xhr_key == 'XMLHttpRequest':

        catalog_btn_template = render_template('includes/catalog_btn_template.html')

        basket_info = render_template(
            'includes/empty_basket.html'
        )

        context = {
            'catalog_btn_template': catalog_btn_template,
            'basket_info': basket_info,
            'clear_cart': True
        }
        return jsonify(context)
    return redirect(url_for('index'))


@bp.route('/delete_product/<product_id>/', methods=['GET', 'POST'])
def delete_product(product_id):
    if 'shopping_cart' in session:
        if product_id in session['shopping_cart']:
            if session['shopping_cart'][product_id] > 1:
                session['shopping_cart'][product_id] -= 1
            else:
                session['shopping_cart'].pop(product_id)

            set_total_price()

            session.modified = True

        # ajax logic
        request_xhr_key = request.headers.get('X-Requested-With')
        if request_xhr_key and request_xhr_key == 'XMLHttpRequest':

            catalog_btn_template = render_template('includes/catalog_btn_template.html', product_id=product_id)

            if session['shopping_cart']:
                basket_info = render_template(
                    'includes/basket.html',
                    product_id=product_id,
                    basket_products=Product.objects(id__in=session['shopping_cart'].keys()),
                    basket_form=BasketForm(),
                )
            else:
                basket_info = render_template(
                    'includes/empty_basket.html'
                )

            context = {
                'catalog_btn_template': catalog_btn_template,
                'basket_info': basket_info
            }
            return jsonify(context)

    return redirect(url_for('index'))
