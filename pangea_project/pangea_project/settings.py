"""
Django settings for pangea project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lt8r99*5j9rb_yd%fqd62hlh*v*7=5fc1*)hjs&bri&$lfn5gt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'charity_app',
    'giver_app',
    'user_app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    's3direct',
    'registration',
    'embed_video',
    'tastypie',
    'tastypie_swagger'
)

AWS_SECRET_ACCESS_KEY = 'hQewlp/tx5114lnfO6FNT7SA+zvxhrtCruQwo6MU'
AWS_ACCESS_KEY_ID = 'AKIAJKNN6S276LTSNWRA'
AWS_STORAGE_BUCKET_NAME = 'uploadedimages123'
S3DIRECT_ENDPOINT = 's3-us-west-1.amazonaws.com'
S3DIRECT_UNIQUE_RENAME = True


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'social.apps.django_app.context_processors.backends',
    'django.core.context_processors.request',
    'social.apps.django_app.context_processors.login_redirect',
)

SOCIAL_AUTH_FACEBOOK_KEY = '1528965467327552'
SOCIAL_AUTH_FACEBOOK_SECRET = '667619f8a2385262098b1638d541170c'


ROOT_URLCONF = 'pangea_project.urls'

WSGI_APPLICATION = 'pangea_project.wsgi.application'

TASTYPIE_FULL_DEBUG = True

TASTYPIE_SWAGGER_API_MODULE = "pangea_project.urls.v1_api"

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pangea_database',
        'USER': "yash",
        'PASSWORD':"",
        "HOST":"127.0.0.1",
        "PORT": ""
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'login'
LOGIN_REDIRECT_URL = "login"
LOGIN_URL = 'auth_login'


import smtplib
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
smtp=smtplib.SMTP(host=EMAIL_HOST,port=EMAIL_PORT)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "foundersofpangea@gmail.com"
EMAIL_HOST_PASSWORD = 'pang3aunit3'

ACCOUNT_ACTIVATION_DAYS=7



AUTHENTICATION_BACKENDS = (
      'social.backends.facebook.FacebookOAuth2',
      'django.contrib.auth.backends.ModelBackend',
)


FACEBOOK_AUTH_EXTRA_ARGUMENTS = {'display': 'popup'}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')