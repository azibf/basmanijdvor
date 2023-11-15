from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Specialization)
admin.site.register(Doctor)
admin.site.register(CEvent)