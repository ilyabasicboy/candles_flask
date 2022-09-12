import os

MEDIA_ROOT = 'media'
UPLOAD_FILE_DIR = os.path.join(MEDIA_ROOT, 'files')

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
