"""
Django settings for understand_science project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
#from dotenv import load_dotenv
import os
import json
import dj_database_url

from os import environ

#load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-r@*&o^cy1nd@&y47ppi7fonorxbfgdmm&&818eb%%m2xqns@7!"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "18.205.155.104",
    "localhost",
    "127.0.0.1",
    "http://uts-portal.s3-website-us-east-1.amazonaws.com/",
    ".awsapprunner.com"
]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "uts.apps.UtsConfig",
    "contacts.apps.ContactsConfig",
    "video_metadata.apps.VideoMetadataConfig",
    "site_admin_settings.apps.SiteAdminSettingsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "understand_science.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "understand_science.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

if "DATABASE_SECRET" in environ:
    database_secret = environ.get("DATABASE_SECRET")
    db_url = json.loads(database_secret)["DATABASE_URL"]
    DATABASES = {"default": dj_database_url.parse(db_url)}
elif "DB_NAME" in environ:
    DATABASES = {
    "default": {
        # "ENGINE": "django.db.backends.mysql",
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": environ["DB_NAME"],
        "USER": environ["DB_USER"],
        "PASSWORD": environ["DB_PASS"],
        "HOST": environ["DB_HOST"],
        "PORT": environ["DB_PORT"],
    }
}
else:
    DATABASES = {"default": dj_database_url.parse("sqlite:///db.sqlite3")}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media").replace("\\", "/")


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ORIGIN_ALLOW_ALL = True

# Email Config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'netsol-smtp-oxcs.hostingplatform.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

if "DATABASE_SECRET" in environ:
    database_secret = environ.get("DATABASE_SECRET")
    EMAIL_HOST_USER = json.loads(database_secret)["EMAIL_HOST_USER"]
    EMAIL_HOST_PASSWORD = json.loads(database_secret)["EMAIL_HOST_PASSWORD"]
    # Django host url config
    HOST_URL = json.loads(database_secret)["HOST_URL"]
else:
    EMAIL_HOST_USER = environ["EMAIL_HOST_USER"]
    EMAIL_HOST_PASSWORD = environ["EMAIL_HOST_PASSWORD"]
    # Django host url config
    HOST_URL = environ["HOST_URL"]
    

AWS_ACCESS_KEY_ID = environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = environ["AWS_SECRET_ACCESS_KEY"]
AWS_STORAGE_BUCKET_NAME = 'uts-static-data'
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = 'us-east-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'