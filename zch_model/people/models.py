#coding:utf-8
from django.db import models
import ast
# Create your models here.
class CompressedTextField(models.TextField):

	def from_db_value(self,value,expression,connection,context):
		if not value:
			return value
		try:
			return value.decode('base64').decode('bz2').decode('utf-8')
		except Exception:
			return value

	def to_python(self,value):
		if not value:
			return value
		try:
			return value.decode('base64').decode('bz2').decode('utf-8')
		except Exception:
			return value

	def get_prep_value(self,value):
		if not value:
			return value
		try:
			value.decode('base64')
			return value.decode('base64')
		except Exception:
			try:
				return value.decode('base64').decode('bz2').decode('utf-8')
			except Exception:
				return value

class Person(models.Model):
	name=models.CharField(max_length=30)
	age=models.IntegerField()
	
	def __str__(self):
		return self.name
	__repr__=__str__

class ListField(models.TextField):
	description="stores a python list"
	
	def __init__(self, *args, **kwargs):
		super(ListField,self).__init__(*args, **kwargs)
	
	def to_python(self, value):
		if not value:
			value=[]
		if isinstance(value, list):
			return value
		return ast.literal_eval(value)
	def get_prep_value(self, value):
		if value is None:
			return value
		return str(value)
	def value_to_string(self, obj):
		value=self._get_val_from_obj(obj)
		return self.get_db_prep_value(value)

class Article(models.Model):
	labels=ListField()
