from django.contrib import admin
from .models import Service, Image, Category
from pillow_heif import register_heif_opener
register_heif_opener()

# Register your models here.

admin.site.register(Service)
admin.site.register(Image)
admin.site.register(Category)