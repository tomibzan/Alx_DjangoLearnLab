"""
Django settings for LibraryProject project.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secret-key-here'

# SECURITY WARNING: don't run with debug turned on in production!
# Set to False in production
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'your-domain.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Content Security Policy Middleware (if using django-csp)
    # 'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Custom User Model
AUTH_USER_MODEL = 'bookshelf.CustomUser'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# === SECURITY SETTINGS ===
# Security settings to protect against common vulnerabilities

# Security Middleware Settings
SECURE_BROWSER_XSS_FILTER = True  # Adds X-XSS-Protection header
SECURE_CONTENT_TYPE_NOSNIFF = True  # Adds X-Content-Type-Options header
X_FRAME_OPTIONS = 'DENY'  # Prevents clickjacking attacks

# HTTPS Settings (set to True in production with HTTPS)
SECURE_SSL_REDIRECT = True  # Redirect all HTTP requests to HTTPS
SECURE_HSTS_SECONDS = 31536000  # 1 year HSTS
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Cookie Security Settings
CSRF_COOKIE_SECURE = True  # CSRF cookies only sent over HTTPS
SESSION_COOKIE_SECURE = True  # Session cookies only sent over HTTPS
CSRF_COOKIE_HTTPONLY = True  # Prevent CSRF cookie access via JavaScript
SESSION_COOKIE_HTTPONLY = True  # Prevent session cookie access via JavaScript

# Additional Security Headers
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'

# === CONTENT SECURITY POLICY SETTINGS ===
# Uncomment and configure if using django-csp package
# CSP_DEFAULT_SRC = ("'self'",)
# CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'")
# CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")
# CSP_IMG_SRC = ("'self'", "data:")
# CSP_FONT_SRC = ("'self'",)
# CSP_CONNECT_SRC = ("'self'",)
