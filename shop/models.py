from django.db import models

# Create your models here.

class Shop(models.Model):
	webname = models.CharField(max_length=20)
	title = models.CharField(max_length=200)
	photo = models.CharField(max_length=200)
	price = models.IntegerField()
	link = models.CharField(max_length=200)
	brand = models.CharField(max_length=11)

	class Meta:
		db_table='shop'
