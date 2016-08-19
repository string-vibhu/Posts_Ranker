from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	text = models.CharField(max_length=2000)
	auth_count = models.IntegerField(default=0,null=True)
	fake_count = models.IntegerField(default=0,null=True)
	comment_count = models.IntegerField(default=0,null=True)
	rating = models.FloatField(default=0,null=True)
	share_count = models.IntegerField(default=0,null=True)
	date = models.DateTimeField()
	rank = models.FloatField(default=0,null=True)

	def __str__(self):
		return self.title

class Weight(models.Model):
	Features=models.CharField(max_length=20)
	weight= models.FloatField(default=0,null=True)

	def __str__(self):
		return self.Features