from flask import (
    Blueprint, flash, redirect, request, url_for
)
from candles.feedback.forms import FeedbackForm

bp = Blueprint('feedback', __name__)


@bp.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm(request.form)
    if request.method == 'POST' and form.validate():
        print('Success')
        return redirect(url_for('products.index'))
    print(form.errors)
    return redirect(url_for('products.index'))
