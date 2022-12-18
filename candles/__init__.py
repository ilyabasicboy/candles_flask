import os
from flask import Flask, render_template
from flask_mail import Mail
from flask.helpers import send_from_directory
from flask_mongoengine import MongoEngine
from flask_admin import Admin
from candles.content.models import Gallery, Product, Advantage, OrderStep, Contact
from candles.auth.models import User
from candles.admin.views import CustomModelView, CustomAdminIndexView, UserAdminView
import flask_login as login


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
    admin.add_view(CustomModelView(User))
    admin.add_view(CustomModelView(Product))
    admin.add_view(CustomModelView(Advantage))
    admin.add_view(CustomModelView(OrderStep))
    admin.add_view(CustomModelView(Gallery))
    admin.add_view(CustomModelView(Contact))


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
        context = {
            'products': Product.objects(),
            'advantages': Advantage.objects(),
            'order_steps': OrderStep.objects(),
            'gallery': Gallery.objects().first(),
            'contacts': Contact.objects(),
            'user': login.current_user,
        }
        return render_template('frontpage.html', **context)

    from candles.feedback import views as feedback
    app.register_blueprint(feedback.bp)

    from candles.shopping_cart import views as shopping_cart
    app.register_blueprint(shopping_cart.bp)

    return app
