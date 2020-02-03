from django.db import models

# Create your models here.

class Champion(models.Model):
    id_champ = models.IntegerField(primary_key=True)
    idreal_champ = models.CharField(max_length=50)
    name_champ = models.CharField(max_length=50)
    iden_champ = models.CharField(max_length=50)
    title_champ = models.CharField(max_length=200)
    tags_champ = models.CharField(max_length=100)
    lore_champ = models.TextField(max_length=999)
