import mongoengine as me


class User(me.Document):
    login = me.StringField(max_length=80, unique=True)
    email = me.StringField(max_length=120)
    password = me.StringField(max_length=64)
    superuser = me.BooleanField()

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    # Required for administrative interface
    def __unicode__(self):
        return self.login
