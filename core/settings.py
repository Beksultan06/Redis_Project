from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-yr1=x6ty#2pxhy11*mhp+b)n65y%gnpte*b)*iqone1&guf*t!"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'jazzmin',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.sites',

    'ckeditor',

    'apps.settings',
    'apps.telegram',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Найдите идентификатор вашего объекта сайта в базе данных и укажите его здесь
SITE_ID = 1

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# redis
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Используйте Redis для хранения сессий
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

# jazzmin
JAZZMIN_SETTINGS = {
    "site_title": "REDIS",  # Заголовок сайта
    "site_header": "REDIS",  # Заголовок на экране входа
    "site_brand": "REDIS",  # Выходит на сайте вместо Django-admin.(Администрирование сайта)
    "welcome_sign": "Добро пожаловать в REDIS",  # Приветственный текст на экране входа
    "copyright": "REDIS",  # Авторское право (footer)


    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://web.telegram.org/k/Bek_sul_t_an", "new_window": True},

    ],

    "show_sidebar": True,

    "changeform_format": "horizontal_tabs",

}


JAZZMIN_UI_TWEAKS = {
    # белый фон:
    # "theme": "flatly",
    # "theme" : "simplex",  # белый фон с цветами - RGB
    # "theme": "sketchy",  #  мультяшный

    # темный фон:
    # "theme": "darkly",
    "theme": "itera",    # темный (серьезный , полностью)

}

APPEND_SLASH = False

# redis
REDIS_PORT = 6379
REDIS_HOST = 'localhost'  # Используйте localhost вместо redis

# celery
CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Используйте localhost вместо redis
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'  # Используйте localhost вместо redis

# ckeditor
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'  # URL to jQuery
CKEDITOR_IMAGE_BACKEND = "pillow"  # Путь к пакету Pillow для обработки изображений
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',  # Вы можете настроить свою собственную панель инструментов CKEditor
        'height': 300,
        'width': 800,
    },
}