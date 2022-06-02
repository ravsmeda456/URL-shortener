from django.db import models

# Create your models here.
class url(models.Model):
    short_url = models.CharField(max_length=200)
    actual_url = models.CharField(max_length=50, unique=True)