"""
Django settings for advanced_features_and_security project.

"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-your-very-long-secret-key-here-change-in-production'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # Set to False in production

# ALLOWED_HOSTS should be configured properly for production
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'yourdomain.com',  # Replace with your actual domain
    'www.yourdomain.com',  # Replace with your actual domain
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Your custom apps would go here
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Add SecurityMiddleware at the top for security headers
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'advanced_features_and_security.urls'

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

WSGI_APPLICATION = 'advanced_features_and_security.wsgi.application'

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
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Custom User Model (if you implemented it from previous task)
# AUTH_USER_MODEL = 'your_app.CustomUser'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ============================================================================
# SECURITY CONFIGURATIONS
# ============================================================================

# HTTPS Configuration
# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS)
# Instruct browsers to only access the site via HTTPS for 1 year (31536000 seconds)
SECURE_HSTS_SECONDS = 31536000
# Include all subdomains in the HSTS policy
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# Allow preloading of HSTS policy
SECURE_HSTS_PRELOAD = True

# Secure Cookies Configuration
# Ensure session cookies are only transmitted over HTTPS
SESSION_COOKIE_SECURE = True
# Ensure CSRF cookies are only transmitted over HTTPS
CSRF_COOKIE_SECURE = True

# Additional Security Headers
# Prevent your site from being framed (clickjacking protection)
X_FRAME_OPTIONS = 'DENY'
# Prevent browsers from MIME-sniffing a response away from the declared content-type
SECURE_CONTENT_TYPE_NOSNIFF = True
# Enable the browser's XSS filtering (Note: Deprecated in modern browsers)
SECURE_BROWSER_XSS_FILTER = True

# Additional Security Settings
# Set the 'Secure' flag on the session cookie
SESSION_COOKIE_HTTPONLY = True
# Set the 'HttpOnly' flag on the CSRF cookie
CSRF_COOKIE_HTTPONLY = True
# Referrer Policy
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'

# ============================================================================
# ENVIRONMENT-SPECIFIC SETTINGS
# ============================================================================

# Development vs Production settings
if DEBUG:
    # Development settings - less strict for easier development
    SECURE_SSL_REDIRECT = False
    SECURE_HSTS_SECONDS = 0
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
else:
    # Production settings - maximum security
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
