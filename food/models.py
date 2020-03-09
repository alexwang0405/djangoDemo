from django.db import models

# Create your models here.
class Food(models.Model):
	link = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	image = models.CharField(max_length=200)
	datetime = models.CharField(max_length=16)

	class Meta:
		db_table='food'
