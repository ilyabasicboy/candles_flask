from flask_admin.contrib.mongoengine import ModelView
import flask_admin as admin
import flask_login as login
from flask_admin import expose
from candles.auth.forms import LoginForm, RegistrationForm
from flask import request, redirect, render_template, url_for
from candles.auth.models import User


# Create customized model view class
class CustomModelView(ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated


# Create customized index view class that handles login & registration
class CustomAdminIndexView(admin.AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(CustomAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        form = LoginForm(request.form)
        if request.method == 'POST' and form.validate():
            user = form.get_user()
            login.login_user(user)
            return redirect(url_for('admin.index'))

        return render_template('auth/login.html', form=form)


    @expose('/admin_register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        if request.method == 'POST' and form.validate():
            user = User(superuser=True)

            form.populate_obj(user)
            user.save()

            login.login_user(user)
            return redirect(url_for('admin.index'))

        return render_template('auth/register.html', form=form)


    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('admin.index'))


# ---- ADMIN VIEWS ----- #
class UserAdminView(CustomAdminIndexView):
    column_editable_list = ['superuser']
