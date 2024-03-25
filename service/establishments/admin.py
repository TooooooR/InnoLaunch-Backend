from django.contrib import admin
from .api.models import (Establishment, Comment, Service,
                         Photo, Price, Address, Amenity)

# Register your models here.
admin.site.register(Establishment)
admin.site.register(Comment)
admin.site.register(Service)
admin.site.register(Photo)
admin.site.register(Price)
admin.site.register(Amenity)
admin.site.register(Address)
