from django.db import models
class User(models.Model):
    image = models.ImageField(upload_to='users/', null=True, blank=True)
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)

# Create your models here.
