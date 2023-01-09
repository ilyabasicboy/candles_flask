from flask import Blueprint, flash, redirect, request, url_for, current_app, render_template, session
from flask_mail import Message, Mail
from candles.feedback.forms import BasketForm, QuestionForm
from candles.content.models import Product
from candles.auth.models import User

bp = Blueprint('feedback', __name__)


@bp.route('/basket_feedback', methods=['GET', 'POST'])
def basket_feedback():
    mail = Mail(current_app)
    form = BasketForm(request.form)

    shopping_cart = session.get('shopping_cart')

    if shopping_cart:
        products = Product.objects(id__in=shopping_cart.keys())
        print(form.validate(), form.errors)
        if request.method == 'POST' and form.validate() and shopping_cart:
            context = {
                'form': request.form,
                'products': products,
                'shopping_cart': shopping_cart
            }

            text = render_template('feedback/basket_form/message.html', **context)
            mailing_list = list(User.objects(superuser=True).values_list('email'))

            msg = Message(
                recipients=mailing_list,
            )
            msg.html = text
            msg.subject = 'Заказ с сайта svechnayalavka-candles.ru'
            mail.send(msg)
            return redirect(url_for('index'))
    return redirect(url_for('index'))



@bp.route('/feedback_question', methods=['GET', 'POST'])
def question_feedback():
    mail = Mail(current_app)
    form = QuestionForm(request.form)

    if request.method == 'POST' and form.validate():
        context = {
            'form': request.form,
        }

        text = render_template('feedback/question_form/message.html', **context)
        mailing_list = list(User.objects(superuser=True).values_list('email'))

        msg = Message(
            recipients=mailing_list,
        )
        msg.html = text
        msg.subject = 'Вопрос с сайта svechnayalavka-candles.ru'
        mail.send(msg)
        return redirect(url_for('index'))
    return redirect(url_for('index'))
