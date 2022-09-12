from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from candles.auth.auth import login_required
from candles.db import get_db
from werkzeug.utils import secure_filename
from candles.config import UPLOAD_FILE_DIR
import os

bp = Blueprint('products', __name__)


@bp.route('/')
def index():
    db = get_db()
    products = db.execute(
        'SELECT p.id, title, description, price, author_id'
        ' FROM product p JOIN user u ON p.author_id = u.id'
        ' ORDER BY p.id DESC'
    ).fetchall()
    return render_template('frontpage.html', products=products)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        image = request.files['image']
        imagename = secure_filename(image.filename)
        image_path = os.path.join(UPLOAD_FILE_DIR, imagename)
        image.save(image_path)
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO product (title, description, price, image, author_id)'
                ' VALUES (?, ?, ?, ?, ?)',
                (title, description, price, image_path, g.user['id'])
            )
            db.commit()
            return redirect(url_for('admin.index'))

    return render_template('/products/create.html')


def get_products(id, check_author=True):
    product = get_db().execute(
        'SELECT p.id, title, description, price, author_id, username'
        ' FROM product p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if product is None:
        abort(404, f"Product id {id} doesn't exist.")

    if check_author and product['author_id'] != g.user['id']:
        abort(403)

    return product


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    product = get_products(id)

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE product SET title = ?, description = ?, price = ?'
                ' WHERE id = ?',
                (title, description, price, id)
            )
            db.commit()
            return redirect(url_for('products.index'))

    return render_template('products/update.html', product=product)


@bp.route('/<int:id>/delete', methods=('POST', 'GET'))
@login_required
def delete(id):
    get_products(id)
    db = get_db()
    db.execute('DELETE FROM product WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('admin.index'))
