from django.db import models

# Create your models here.

class crud(models.Model):
    password = models.TextField(max_length=255)