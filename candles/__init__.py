import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask.helpers import send_from_directory

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'candles.sqlite'),
    )
    app.config['UPLOAD_FOLDER'] = os.path.join(app.instance_path, 'media')

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)\

    @app.route('/media/<path:filename>')
    def media(filename):
        upload_folder = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
        print(upload_folder)
        return send_from_directory(upload_folder, filename)

    from candles.auth import auth
    app.register_blueprint(auth.bp)

    from candles.products import products
    app.register_blueprint(products.bp)
    app.add_url_rule('/', endpoint='index')

    from candles.admin import admin
    app.register_blueprint(admin.bp)

    return app
