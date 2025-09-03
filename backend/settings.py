import dj_database_url
from decouple import config
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config("DJANGO_SECRET_KEY", default="unsafe-secret-key")


DEBUG = config("DEBUG", default=False, cast=bool)   


ALLOWED_HOSTS = [
    "unima-notes.vercel.app",       
    "notesdigitalbrainslab.onrender.com",          
    "localhost", "127.0.0.1"         
]


INSTALLED_APPS = [
    'users',
    'notesPage',
    'corsheaders',        
    'rest_framework',
    'rest_framework.authtoken',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  
    "corsheaders.middleware.CorsMiddleware",       
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


if config("DATABASE_URL",default=None):
  DATABASES = {
    'default': dj_database_url.parse(
        config("DATABASE_URL", default=f"sqlite:///{BASE_DIR}/db.sqlite3"), 
        conn_max_age=600,
        ssl_require=True if not DEBUG else False   
    )
}
else:
  DATABASES ={
    'default':{
      'ENGINE':'django.db.backends.sqlite3',
      'NAME':BASE_DIR/"db.sqlite3",
    }
  }
     


AUTH_PASSWORD_VALIDATORS = [
    {"NAME": 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {"NAME": 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {"NAME": 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {"NAME": 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"  # 👉 Added for optimized static serving

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'users.CustomUser'


CORS_ALLOWED_ORIGINS = [
    "https://unima-notes.vercel.app",   
    "http://localhost:3000",            
]




