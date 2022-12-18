# Create dummy secrey key so we can use sessions
SECRET_KEY = 'dev'

# Create in-memory database
MONGODB_SETTINGS = {
    "db": "candles",
}

MAIL_SERVER = 'smtp.yandex.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'candles-magazine@yandex.ru'
MAIL_PASSWORD = 'Ahehyhama1'
MAIL_DEFAULT_SENDER = MAIL_USERNAME
