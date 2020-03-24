from django.db import models

# Create your models here.
class Book(models.Model):
    kind = models.CharField(max_length=7)
    link = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    price = models.IntegerField()

    class Meta:
        db_table='book'
