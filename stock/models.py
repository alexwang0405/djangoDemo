from django.db import models

# Create your models here.

class Stock(models.Model):
	name = models.CharField(max_length=10)
	no = models.CharField(max_length=4)
	openprice = models.FloatField()
	endprice = models.FloatField()
	date = models.CharField(max_length=9)
	
	class Meta:
		db_table='stock'
