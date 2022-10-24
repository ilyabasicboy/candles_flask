from flask import Blueprint, render_template
import flask_login as login
from candles.products.models import Product

bp = Blueprint('products', __name__)


@bp.route('/')
def index():
    products = Product.objects()
    return render_template('frontpage.html', products=products, user=login.current_user)
