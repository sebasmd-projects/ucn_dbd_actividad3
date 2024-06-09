import logging
from pathlib import Path

import environ
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext_lazy as _

from .settings_config import (settings_apps, settings_locale_paths,
                              settings_middleware, settings_rest)

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent

LOCALE_PATHS = settings_locale_paths.LOCALE_PATHS

# Log Reports
logging.basicConfig(
    filename='stderr.log', format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8'
)

# Environment config
env = environ.Env(
    # Custom env, local, qa, prod
    ENVIRONMENT=(str, 'local'),

    # Django secret key
    SECRET_KEY=(
        str, 'custom-secret-django-key'
    ),

    # Rest and IPs
    ALLOWED_HOSTS=(list, ['127.0.0.1', 'localhost']),
    INTERNAL_IPS=(list, ['localhost', '127.0.0.1', '0.0.0.0']),
    DOMAIN=(str, 'localhost:8000'),
    CORS_ALLOWED_ORIGINS=(
        list, [
            'http://localhost:3000'
        ]
    ),

    # Internationalization
    LANGUAGE_CODE=(str, 'es'),
    TIME_ZONE=(str, 'America/Bogota'),

    # Database config
    DB_NAME=(str, 'ecommerce_dev'),
    DB_USER=(str, 'ecommerce_dev_db_user'),
    DB_PASSWORD=(str, 'ecommerce_dev_db_password'),
    DB_HOST=(str, 'localhost'),
    DB_PORT=(int, 5432),
    DB_CONN_MAX_AGE=(int, 60),
    DB_CHARSET=(str, 'UTF8'),

    # Email config
    EMAIL_BACKEND=(str, 'django.core.mail.backends.smtp.EmailBackend'),
    DEFAULT_FROM_EMAIL=(
        str, f'Ecommerce | <noreply@domain.com>'
    ),
    SERVER_EMAIL=(str, 'noreply@domain.com'),
    SERVER_ADMIN=(str, 'support@domain.com'),
    YASG_EMAIL=(str, 'support@domain.com'),
    EMAIL_SECURITY_CONNECTION=(str, 'TLS'),
    EMAIL_PORT=(int, 587),
    EMAIL_TIMEOUT=(int, 300),
    EMAIL_HOST_USER=(str, 'noreply@domain.com'),
    EMAIL_HOST_PASSWORD=(str, 'email_password'),

    # Custom config
    ADMIN_URL=(str, 'admin/'),
    ERROR_TEMPLATE=(str, 'errors_template.html'),
    UTILS_PATH=(str, 'apps.common.utils'),
    YASG_TERMS_OF_SERVICE=(str, 'https://www.domain.com/policies/terms/'),
    MIDDLEWARE_NOT_INCLUDE=(list, [
        '/api/v1/logs/log/remove/1/',
        '/api/v1/logs/log/',
        '/api/v1/logs/',
        '/api/redoc/',
        '/api/docs/',
    ]),
)


environ.Env.read_env((BASE_DIR / '.env'))

ENVIRONMENT = env(
    'ENVIRONMENT'
)

# Security
if ENVIRONMENT.lower() in ['local', 'qa']:
    DEBUG = True
    LOGOUT_REDIRECT_URL = '/'
    LOGIN_REDIRECT_URL = '/'
else:
    DEBUG = False
    SESSION_COOKIE_HTTPONLY = True
    CSRF_COOKIE_HTTPONLY = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'DENY'

APPEND_SLASH = True

# Django secret key
SECRET_KEY = env(
    'SECRET_KEY'
)

# YASG tyc
# TODO terms_of_service YASG
YASG_TERMS_OF_SERVICE = env(
    'YASG_TERMS_OF_SERVICE'
)

YASG_EMAIL = env(
    'YASG_EMAIL'
)

# Django internationalization
LANGUAGE_CODE = env(
    'LANGUAGE_CODE'
)

TIME_ZONE = env(
    'TIME_ZONE'
)

LANGUAGES = [
    ('es', _('Español')),
    ('en', _('Ingles'))
]

PARLER_LANGUAGES = {
    None: (
        {'code': 'es', },
        {'code': 'en', },
    ),
    'default': {
        'fallbacks': ['es'],
        'hide_untranslated': False,
    }
}

USE_I18N = True

USE_L10N = True

USE_TZ = True

ROSETTA_SHOW_AT_ADMIN_PANEL = True

# Allowed Hosts
ALLOWED_HOSTS = env.list(
    'ALLOWED_HOSTS'
)

INTERNAL_IPS = env.list(
    'INTERNAL_IPS'
)

# Apps
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.postgres',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps'
]

THIRD_APPS = settings_apps.THIRD_APPS

CUSTOM_APPS = settings_apps.CUSTOM_APPS

INSTALLED_APPS = THIRD_APPS + DJANGO_APPS + CUSTOM_APPS

UTILS_PATH: str = env(
    'UTILS_PATH'
)

if UTILS_PATH is None:
    raise ImproperlyConfigured('The UTILS_PATH variable is not defined')

UTILS_DATA_PATH = f"{UTILS_PATH.replace('.', '\\')}\\data"

SITE_ID = 1

DOMAIN = env(
    'DOMAIN'
)

# Middleware
MIDDLEWARE = settings_middleware.MIDDLEWARE

MIDDLEWARE_NOT_INCLUDE = env(
    'MIDDLEWARE_NOT_INCLUDE'
)

# Url config
ROOT_URLCONF = 'app_core.urls'

ADMIN_URL = env(
    'ADMIN_URL'
)

# Templates config
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'app_core' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                f'{UTILS_PATH}.context_processors.custom_processors'
            ],
        },
    },
]

ERROR_TEMPLATE = env(
    'ERROR_TEMPLATE'
)

# Server Gateway Interface
ASGI_APPLICATION = 'app_core.asgi.application'

# Database config
DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
        'CONN_MAX_AGE': env('DB_CONN_MAX_AGE'),
        'CHARSET': env('DB_CHARSET'),
        'ATOMIC_REQUESTS': True
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Auth
AUTH_USER_MODEL = 'users.UserModel'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    f'{UTILS_PATH}.backend.EmailOrUsernameModelBackend',
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# Static & Media ROOT
STATIC_ROOT = str(BASE_DIR / 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = [str(BASE_DIR / 'app_core' / 'static')]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

MEDIA_ROOT = str(BASE_DIR / 'app_core' / 'media')

MEDIA_URL = "/media/"

# STORAGE CAHCHING
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

WHITENOISE_MANIFEST_STRICT = False

# Rest
SWAGGER_SETTINGS = settings_rest.SWAGGER_SETTINGS

REST_FRAMEWORK = settings_rest.REST_FRAMEWORK

CORS_ALLOWED_ORIGINS = env('CORS_ALLOWED_ORIGINS')

SIMPLE_JWT = settings_rest.SIMPLE_JWT

# Utils
GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}
