from django.db import models


# Create your models here.
class Article(models.Model):
	title=models.CharField(u'headline',max_length=256)
	content=models.TextField(u'content')

	pub_date=models.DateTimeField(u'publish time',auto_now_add=True, editable=True)
	update_time=models.DateTimeField(u'update time',auto_now=True,null=True)
	def __str__(self):
		return self.title
	search_fields=('title','content',)
class Person(models.Model):
	name=models.CharField(u'class_name',max_length=256)
	age=models.IntegerField(u'age')
	def __str__(self):
		return self.name
