from django.db import models

# Create your models here.
class Chmapion(models.Model):
    idchamp = models.IntegerField(primary_key=True)
    namechamp = models.CharField(max_length=50)
    namechampbase = models.CharField(max_length=50)
