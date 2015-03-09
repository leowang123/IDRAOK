from django.db import models

# Create your models here.

class Article(models.Model):		#post an article, record title, how many likes
	title = models.CharField(max_length=200)	#char max length is 200
	body =models.TextField()
	pub_date = models.DateTimeField('date published')
	likes = models.IntegerField()

	
	
