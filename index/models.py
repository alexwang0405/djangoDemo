from django.db import models

# Create your models here.

class Home(models.Model):
    image = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    class Meta:
        db_table='home'
