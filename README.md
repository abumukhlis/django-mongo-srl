Django-Mongo Setup Wiki for Space Rendition Learning

Instructions for setting up Django projects.

Table of Contents

General Setup for all Django Projects
Django REST Framework
Django GraphQL
Django MongoDB
Full-Stack Django (with templates)

General Setup for all Django Projects

Recommended Technologies
Django 3.x
Mongodb, Mongodb Compass or Mongodb Atlas
Poetry
#Postgres: You can use MySQL or SQL Lite, but Postgres is recommended by the Django official docs. The only #exception is if you want to use MongoDB or another NoSQL database with your project. You can find details for #that below.
Initial Setup
Must have Python 3, Django, and Mongodb installed

Make sure Mongodb is running on your machine

django-admin startproject [projectname]

Create a virtual environment: python -m venv venv

Go into your virtual environment: source venv/bin/activate

Run poetry init -> This will create a TOML file for you with your project config where Poetry will add your dependencies

Install djongo: poetry add djongo

Rename the [projectname] folder to config

Create a folder named apps

Create an __init__.py file inside of the apps folder

Users Setup

Create a users app: mkdir apps/users and then [python manage.py startapp users apps/users]

Add "users app" to settings.py as "apps.users" and in apps.py file, change the name attribute to "apps.users"
Setup custom User model and custom user manager: https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#a-full-example

Add the code below to the settings.py file
AUTH_USER_MODEL = 'users.User'



Set up admin interface for User model:
from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_admin')


admin.site.register(User, UserAdmin
Database Setup
Postgres is optional, but recommended in the official Django docs.

Setup Postgres in Django settings.py file:
'default': {
    'ENGINE': 'djongo',
    'NAME': '[dbname]',
    
}
Run migrations: python manage.py migrate
More Setup
Create an admin user for logging into the Django admin interface: python manage.py createsuperuser
Run the app: python manage.py runserver
View the API at localhost:8000 and the admin interface at localhost:8000/admin
