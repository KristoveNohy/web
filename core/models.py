from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    details = models.TextField()
    cover_image = models.ImageField(upload_to='services/')

class Project(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    details = models.TextField()
    location = models.CharField(max_length=300)
    media_folder = models.CharField(max_length=300)

class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    rating = models.IntegerField()
    review_text = models.TextField()