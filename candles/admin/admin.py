import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from candles.db import get_db
from candles.auth.auth import login_required


bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
@login_required
def index():
    db = get_db()
    products = db.execute(
        'SELECT p.id, title, description, price, author_id'
        ' FROM product p JOIN user u ON p.author_id = u.id'
        ' ORDER BY p.id DESC'
    ).fetchall()
    return render_template('admin/index.html', products=products)
