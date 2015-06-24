#coding:utf-8
"""
Django settings for emilepy project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#add#################################################
import os.path
import sae.const  
from os import environ  
debug = not environ.get("APP_NAME", "")   
    
MYSQL_HOST = 'w.rdc.sae.sina.com.cn'      
MYSQL_PORT = '3307'   
MYSQL_DB = 'app_emilepy'      
MYSQL_USER = 'zzokok53wk'   
MYSQL_PASS = '5kki0kxi2jj0m3xh421yzkhz243hizxkhjxx0l42'   
    
 


#add######################################################

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j$fb(tm!1upjwoq$ct*65uq%id*y)!uj55r_5!t@ttu2couc-l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#	'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'emilepy.urls'

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

WSGI_APPLICATION = 'emilepy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

#DATABASES = {
#   'default': {
#       'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

#add#####################################################

import sae
from sae._restful_mysql import monkey
monkey.patch()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': MYSQL_DB, 
        'USER': MYSQL_USER, 
        'PASSWORD': MYSQL_PASS, 
        'HOST': MYSQL_HOST, 
        'PORT': MYSQL_PORT, 
    }
}

#add#####################################################

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'


#template
#TEMPLATE_DIRS= (
 #        'd:/mysae/2/blog/templates',
#           os.path.join(BASE_DIR, 'templates'),
#		   os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
#)