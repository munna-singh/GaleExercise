from django.db import models

# Create your models here.

class Writer(models.Model):
	title = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	publication = models.DateTimeField()
	catagory = models.CharField(max_length=50)
	thumbnail = models.CharField(max_length=300)
	large_image = models.CharField(max_length=300)
	description = models.CharField(max_length=10000)
	def __unicode__(self):
		return self.title
