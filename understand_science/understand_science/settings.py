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
    "https://m3qpmwgpm6.us-east-1.awsapprunner.com",
    ".awsapprunner.com"
]
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
    "whitenoise.middleware.WhiteNoiseMiddleware",
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

DATABASES = {
    "default": {
        # "ENGINE": "django.db.backends.mysql",
        'ENGINE': 'django.db.backends.postgresql',
        # "NAME": os.environ["DB_NAME"],
        # "USER": os.environ["DB_USER"],
        # "PASSWORD": os.environ["DB_PASS"],
        # "HOST": os.environ["DB_HOST"],
        # "PORT": os.environ["DB_PORT"],
        "NAME": "uts",
        "USER": "postgres",
        "PASSWORD":"uts#1234",
        "HOST": "uts2.cto0kwugu3a1.us-east-1.rds.amazonaws.com",
        "PORT": "5432"
        
    }
}


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

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ORIGIN_ALLOW_ALL = True

# Email Config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Gmail SMTP server
EMAIL_PORT = 587  # Port for Gmail SMTP
EMAIL_USE_TLS = True  # Enable TLS for secure connection
# EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]  # Your Gmail address
# EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]  # Your Gmail password or application-specific password
# DEFAULT_FROM_EMAIL = os.environ["DEFAULT_FROM_EMAIL"]  # Default sender email address

EMAIL_HOST_USER='understandthesciencedev@gmail.com'  # Your Gmail address
EMAIL_HOST_PASSWORD='cclbamddtjnpwqpg'  # Your Gmail password or application-specific password
DEFAULT_FROM_EMAIL='understandthesciencedev@gmail.com'  # Default sender email address
