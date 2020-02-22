from django.db import models

# Create your models here.

class Stock(models.Model):
	name=models.CharField(max_length=10)
	datetime=models.CharField(max_length=10)
	price=models.FloatField()

	class Meta:
		db_table='stock'
