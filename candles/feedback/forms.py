import wtforms
from flask_wtf import FlaskForm

class BasketForm(FlaskForm):
    name = wtforms.StringField('Ваше имя:', [wtforms.validators.DataRequired()])
    email = wtforms.StringField('E-mail:', [wtforms.validators.Email()])
    phone = wtforms.StringField('Телефон:', [wtforms.validators.DataRequired()])
    comment = wtforms.TextAreaField('Комментарий:', [wtforms.validators.Length(max=800)])
    city = wtforms.StringField('Город:', [wtforms.validators.DataRequired()])
    address = wtforms.TextAreaField('Адрес:', [wtforms.validators.Length(max=800), wtforms.validators.DataRequired()])
    post_index = wtforms.StringField('Почтовый индекс:', [wtforms.validators.Length(max=7)])


class QuestionForm(FlaskForm):
    name = wtforms.StringField('Ваше имя:', [wtforms.validators.DataRequired()])
    email = wtforms.StringField('E-mail:', [wtforms.validators.Email()])
    phone = wtforms.IntegerField('Телефон:', [wtforms.validators.DataRequired()])
    question = wtforms.TextAreaField('Задайте ваш вопрос:', [wtforms.validators.Length(max=800), wtforms.validators.DataRequired()])
