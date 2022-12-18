from flask import Blueprint, flash, redirect, request, url_for, current_app, render_template, session
from flask_mail import Message, Mail
from candles.feedback.forms import FeedbackForm
from candles.content.models import Product
from candles.auth.models import User

bp = Blueprint('feedback', __name__)


@bp.route('/feedback', methods=['GET', 'POST'])
def feedback():
    mail = Mail(current_app)
    form = FeedbackForm(request.form)

    shopping_cart = session.get('shopping_cart')

    if shopping_cart:
        products = Product.objects(id__in=shopping_cart.keys())

    if request.method == 'POST' and form.validate() and shopping_cart:
        context = {
            'form': request.form,
            'products': products,
            'shopping_cart': shopping_cart
        }

        text = render_template('feedback/message.html', **context)
        mailing_list = list(User.objects(superuser=True).values_list('email'))
        msg = Message(
            recipients=mailing_list,
        )
        msg.html = text
        msg.subject = 'Заказ с сайта svechnayalavka-candles.ru'
        mail.send(msg)
        return redirect(url_for('index'))
    return redirect(url_for('index'))
