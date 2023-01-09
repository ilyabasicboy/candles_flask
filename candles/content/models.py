import mongoengine as me
from codecs import encode


class Media(me.EmbeddedDocument):
    title = me.StringField()
    image = me.ImageField(collection_name='image')

    def get_image(self):
        if self.image:
            base64_data = encode(self.image.read(), 'base64')
            image = base64_data.decode('utf-8')
            return image
        else:
            return None


class File(me.EmbeddedDocument):
    title = me.StringField()
    file = me.FileField(
        collection_name='file'
    )

    def get_file(self):
        if self.file:
            base64_data = self.file.read()
            file = base64_data.decode('utf-8')
            return file
        else:
            return None


class Product(me.Document):
    title = me.StringField(required=True)
    subtitle = me.StringField(required=False)
    price = me.IntField(required=True)
    description = me.StringField()
    show = me.BooleanField(default=True)
    images = me.ListField(me.EmbeddedDocumentField(Media))


class Item(me.EmbeddedDocument):
    text = me.StringField(required=True)


class Advantage(me.Document):
    title = me.StringField(required=True)
    items = me.ListField(me.EmbeddedDocumentField(Item))
    description = me.StringField()
    image = me.EmbeddedDocumentField(Media)


class OrderStep(me.Document):
    title = me.StringField(required=True)
    description = me.StringField()
    image = me.EmbeddedDocumentField(File)


class Gallery(me.Document):
    gallery_title = me.StringField(required=True)
    images = me.ListField(me.EmbeddedDocumentField(Media))


class Contact(me.Document):
    title = me.StringField()
    link = me.StringField(required=True)
    icon = me.EmbeddedDocumentField(File)
