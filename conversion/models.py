from django.db import models

# Create your models here.

class Convert(models.Model):
	words = models.TextField() 
	date  = models.DateTimeField(auto_now_add=True)


