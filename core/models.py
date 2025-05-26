from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    details = models.TextField()
    image = models.ImageField(upload_to='static/services/', blank=True, null=True)

class Realization(models.Model):
    category = models.ForeignKey(Service, on_delete=models.CASCADE)
    details = models.TextField()
    location = models.CharField(max_length=300)
    before_image = models.ImageField(upload_to='static/Realization/', blank=True, null=True)
    after_image = models.ImageField(upload_to='static/Realization/')

class Review(models.Model):
    project = models.ForeignKey(Realization, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    rating = models.IntegerField()
    review_text = models.TextField()

class Customer(models.Model):
    fname = models.CharField(max_length=64)
    lname = models.CharField(max_length=64)
    adress = models.CharField(max_length=64)

    email = models.EmailField()
    phone = models.CharField(max_length=13)

    category = models.ForeignKey(Service, on_delete=models.CASCADE)
    details = models.TextField()

