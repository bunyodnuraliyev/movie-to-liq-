from django.contrib import admin
from .models import *
admin.site.register([Actor, Movie, Comment])
