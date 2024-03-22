from django.contrib import admin
from .models import Establishment, Comment, Service, Type

# Register your models here.
admin.site.register(Establishment)
admin.site.register(Comment)
admin.site.register(Type)
admin.site.register(Service)