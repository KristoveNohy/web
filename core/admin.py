from django.contrib import admin
from .models import Service, Image, Category, Customer

# Register your models here.

admin.site.register(Service)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Customer)