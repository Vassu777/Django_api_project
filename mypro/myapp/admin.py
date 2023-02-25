from django.contrib import admin

# Register your models here.
from myapp.models import candidate
from .models import *
# Register your models here.
admin.site.register(candidate)