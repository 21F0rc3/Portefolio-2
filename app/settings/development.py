from app.settings.common import *
import json

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dx9z&=abfi6^3_g=9ia^0ypw1ixfc_hct-8rx2gqd)$46nv2r8'

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1'
]

CSRF_TRUSTED_ORIGINS = [

]


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

with open(os.path.join(BASE_DIR, '../secrets.json')) as secrets_file:
    secrets = json.load(secrets_file)

def get_secret(setting, secrets=secrets):
    """Get secret setting or fail with ImproperlyConfigured"""
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portefolio',
        'USER': 'postgres',
        'PASSWORD': get_secret('DB_PASSWORD'),
        'HOST': 'localhost',
    }
}