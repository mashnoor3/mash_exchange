from django.db import models

# Create your models here.
class Profile(models.Model):
	name = models.CharField(max_length=120)
	location = models.CharField(max_length=120, default='description default text', blank=True, null=True )


	def __unicode__(self):
		return self.name 

	def __str__(self):
		return self.name 

