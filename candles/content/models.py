import mongoengine as me
from codecs import encode


class Media(me.EmbeddedDocument):
    title = me.StringField(
        verbose_name=u'Заголовок',
        help_text=u'Заголовок изображения отображается как всплывающая подсказка.'
    )
    image = me.ImageField(
        collection_name='image',
        verbose_name=u'Изображение',
    )

    def get_image(self):
        if self.image:
            base64_data = encode(self.image.read(), 'base64')
            image = base64_data.decode('utf-8')
            return image
        else:
            return None


class File(me.EmbeddedDocument):
    title = me.StringField(
        verbose_name=u'Заголовок',
    )
    file = me.FileField(
        collection_name='file',
        verbose_name=u'Файл',
    )

    def get_file(self):
        if self.file:
            base64_data = self.file.read()
            file = base64_data.decode('utf-8')
            return file
        else:
            return None


class Product(me.Document):
    title = me.StringField(
        verbose_name=u'Название',
        required=True
    )
    subtitle = me.StringField(
        required=False,
        verbose_name=u'Подзаголовок',
    )
    description = me.StringField(
        verbose_name=u'Описание',
    )
    price = me.IntField(
        required=True,
        verbose_name=u'Цена',
    )
    show = me.BooleanField(
        default=True,
        verbose_name=u'Отображать',
    )
    images = me.ListField(
        me.EmbeddedDocumentField(Media),
        verbose_name=u'Изображение',
    )


class Item(me.EmbeddedDocument):
    text = me.StringField(
        required=True,
        verbose_name=u'Текст',
    )


class Advantage(me.Document):
    title = me.StringField(
        required=True,
        verbose_name=u'Заголовок',
    )
    items = me.ListField(
        me.EmbeddedDocumentField(Item),
        verbose_name=u'Подпункты',
        help_text=u'Подпункты отображаются с символом "-", как список. '
                  u'Нужно добавлять либо подпункты, '
                  u'либо описание к каждому преимуществу.'
    )
    description = me.StringField(
        verbose_name=u'Описание',
    )
    image = me.EmbeddedDocumentField(
        Media,
        verbose_name=u'Изображение',
    )


class OrderStep(me.Document):
    title = me.StringField(
        required=True,
        verbose_name=u'Заголовок',
    )
    description = me.StringField(
        verbose_name=u'Описание',
    )
    image = me.EmbeddedDocumentField(
        File,
        verbose_name=u'svg изображение',
    )


class Gallery(me.Document):
    gallery_title = me.StringField(
        required=True,
        verbose_name=u'Заголовок',
    )
    images = me.ListField(
        me.EmbeddedDocumentField(Media),
        verbose_name=u'Изображение',
    )


class Contact(me.Document):
    title = me.StringField(
        verbose_name=u'Заголовок(всплывающая подсказка)',
    )
    link = me.StringField(
        required=True,
        verbose_name=u'Ссылка',
    )
    icon = me.EmbeddedDocumentField(
        File,
        verbose_name=u'Svg иконка',
    )
