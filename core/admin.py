from django.contrib import admin
from .models import Service, Realization, Review, Customer

# Register your models here.

admin.site.register(Service)
admin.site.register(Realization)
admin.site.register(Review)
admin.site.register(Customer)