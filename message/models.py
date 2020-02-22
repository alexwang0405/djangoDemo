from django.db import models

# Create your models here.

class Message(models.Model):
	title=models.CharField(max_length=200)
	name=models.CharField(max_length=200)
	content=models.CharField(max_length=200)
	datetime=models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table='message'
