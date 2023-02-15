import os
from flask import Flask, render_template, request
from flask.helpers import send_from_directory
from flask_mongoengine import MongoEngine
from flask_admin import Admin
from candles.content.models import Gallery, Product, Advantage, OrderStep, Contact
from candles.auth.models import User
from candles.admin.views import AdminModelView, CustomAdminIndexView, UserAdminView
import flask_login as login
from candles.feedback.forms import BasketForm, QuestionForm


def create_app():
    # create and configure the app

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(os.path.join(app.root_path, 'config.py'))
    app.config['UPLOAD_FOLDER'] = os.path.join(app.instance_path, 'media')

    # flask-mongoengine
    db = MongoEngine(app)

    #----- FLASK-LOGIN -----#

    # Initialize flask-login
    def init_login():
        login_manager = login.LoginManager()
        login_manager.setup_app(app)

        # Create user loader function
        @login_manager.user_loader
        def load_user(user_id):
            return User.objects(id=user_id).first()

    # Initialize flask-login
    init_login()

    #----- FLASK-ADMIN -----#

    admin = Admin(app, 'Candles magazine', index_view=CustomAdminIndexView(), template_mode='bootstrap4')
    admin.add_view(
        AdminModelView(
            User,
            name=u'Пользователи',
        )
    )
    admin.add_view(
        AdminModelView(
            Advantage,
            name=u'О наших изделиях',
        )
    )
    admin.add_view(
        AdminModelView(
            Product,
            name=u'Каталог',
        )
    )
    admin.add_view(
        AdminModelView(
            OrderStep,
            name=u'Как заказать'
        )
    )
    admin.add_view(
        AdminModelView(
            Gallery,
            name=u'Галерея'
        )
    )
    admin.add_view(
        AdminModelView(
            Contact,
            name=u'Контакты'
        )
    )


    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # views
    @app.route('/media/<path:filename>')
    def media(filename):
        upload_folder = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
        return send_from_directory(upload_folder, filename)

    @app.route('/')
    def index():
        ip_address = request.headers.get('X-Real-IP', request.remote_addr)
        context = {
            'products': Product.objects(),
            'advantages': Advantage.objects(),
            'order_steps': OrderStep.objects(),
            'gallery': Gallery.objects().first(),
            'contacts': Contact.objects(),
            'user': login.current_user,
            'basket_form': BasketForm(),
            'question_form': QuestionForm()
        }
        return render_template('frontpage/frontpage.html',ip_address=ip_address, **context)

    from candles.feedback import views as feedback
    app.register_blueprint(feedback.bp)

    from candles.shopping_cart import views as shopping_cart
    app.register_blueprint(shopping_cart.bp)

    return app
