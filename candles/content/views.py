from flask import Blueprint, request, abort, Response
import gridfs
from mongoengine.connection import get_db
from bson.objectid import ObjectId
from PIL import Image
from io import BytesIO


bp = Blueprint('content', __name__)


@bp.route('/files/', methods=['GET'])
def api_file_view():
    pk = request.args.get('id')
    coll = request.args.get('coll')
    db = request.args.get('db', 'default')

    if not pk or not coll or not db:
        abort(404)

    fs = gridfs.GridFS(get_db(db), coll)

    data = fs.get(ObjectId(pk))
    if not data:
        abort(404)

    return Response(
        data.read(),
        content_type=data.content_type,
        headers={'Content-Length': data.length}
    )


@bp.route('/images/', methods=['GET'])
def api_images_view():
    pk = request.args.get('id')
    coll = request.args.get('coll', 'image')
    db = request.args.get('db', 'default')

    if not pk or not coll or not db:
        abort(404)

    fs = gridfs.GridFS(get_db(db), coll)

    data = fs.get(ObjectId(pk))

    if not data:
        abort(404)

    image = Image.open(data)

    # resize image
    width = request.args.get('width', 0)
    height = request.args.get('height', 0)

    try:
        width = int(width)
        height = int(height)
    except ValueError:
        print('width or height is invalid number')

    if width or height:
        if not width:
            width = image.width
        if not height:
            height = image.height
        image.thumbnail((width, height))

    image_io = BytesIO()
    image.save(image_io, format='jpeg')

    return Response(
        image_io.getvalue(),
        content_type=data.content_type,
        headers={'Content-Length': data.length}
    )
