import mongoengine as me
from codecs import encode


class Media(me.EmbeddedDocument):

    title = me.StringField()
    image = me.ImageField(collection_name='image')


    def get_image(self):
        base64_data = encode(self.image.read(), 'base64')
        image = base64_data.decode('utf-8')
        return image


class Product(me.Document):
    title = me.StringField(required=True)
    price = me.IntField(required=True)
    description = me.StringField()
    images = me.ListField(me.EmbeddedDocumentField(Media))
