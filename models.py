from django.db import models

# Create your models here.

class movies(models.Model):
	name = models.CharField(max_length = 100)
	rating = models.DecimalField(max_digits=5, decimal_places=1)
	cast = models.TextField(null = True)
	def __str__(self):
		st = ""
		st += self.name
		st += " "
		st += str(self.rating)
		st += " "
		st += str(self.cast)
		return st