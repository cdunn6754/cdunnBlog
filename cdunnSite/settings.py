"""
Django settings for cdunnSite project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Local settings, to facilitate production and developement git branches
import cdunnSite.localsettings as ls

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = ls.BASE_DIR
TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")
TTT_BUILD_DIR = os.path.join(BASE_DIR, "ticTacToe", "ttt-frontend", "build")


LOGIN_REDIRECT_URL = "/"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ls.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ls.DEBUG

ALLOWED_HOSTS = ls.ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    
    'blogUser',
    'content',
    'ticTacToe',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cdunnSite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, TTT_BUILD_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cdunnSite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = ls.DATABASES


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATICFILES_DIRS = ls.STATICFILES_DIRS

STATIC_ROOT = ls.STATIC_ROOT

STATIC_URL = ls.STATIC_URL

## Media files
MEDIA_ROOT = ls.MEDIA_ROOT

MEDIA_URL = ls.MEDIA_URL

## Security Settings

# Prevent MIME type sniffing, lock content type header
SECURE_CONTENT_TYPE_NOSNIFF = ls.SECURE_CONTENT_TYPE_NOSNIFF

# turn on xss attack filtering
SECURE_BROWSER_XSS_FILTER = ls.SECURE_BROWSER_XSS_FILTER

SESSION_COOKIE_SECURE = ls.SESSION_COOKIE_SECURE


CSRF_COOKIE_SECURE = ls.CSRF_COOKIE_SECURE

X_FRAME_OPTIONS = ls.X_FRAME_OPTIONS

# Nginx is configured to reroute to HTTPS
SECURE_SSL_REDIRECT = ls.SECURE_SSL_REDIRECT

# CORS
CORS_ORIGIN_WHITELIST = ('localhost:3000', )
