from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Women)
admin.site.register(Comment)

admin.site.site_title = 'Админ-Панель'