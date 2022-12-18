import wtforms


class FeedbackForm(wtforms.Form):
    name = wtforms.StringField('Ваше имя', [wtforms.validators.DataRequired()])
    email = wtforms.StringField('E-mail', [wtforms.validators.Email()])
    phone = wtforms.IntegerField('Телефон', [wtforms.validators.DataRequired()])
    comment = wtforms.TextAreaField('Комментарий', [wtforms.validators.Length(max=800)])
    address = wtforms.TextAreaField('Адрес', [wtforms.validators.Length(max=800)])
