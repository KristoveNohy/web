from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    details = models.TextField()
    image = models.ImageField(upload_to='static/services/', blank=True, null=True)

class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Image(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="images")
    images = models.ImageField(upload_to="static/uploads/")

class Customer(models.Model):
    fname = models.CharField(max_length=64)
    lname = models.CharField(max_length=64)
    address = models.CharField(max_length=64)

    email = models.EmailField()
    phone = models.CharField(max_length=16)

    category = models.ForeignKey(Service, on_delete=models.CASCADE)
    details = models.TextField()

