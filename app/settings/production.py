from app.settings.common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = [
    '0.0.0.0',
    'sheltered-bastion-64341.herokuapp.com',
]

CSRF_TRUSTED_ORIGINS = [
    'https://sheltered-bastion-64341.herokuapp.com'
]


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config()
}