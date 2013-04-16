from django.db import models
from django.db.models import permalink
from django.forms import ModelForm
from django import forms

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	posted = models.DateField(db_index=True, auto_now_add=True)
	category = models.ForeignKey('Category')

	def __unicode__(self):
		return '%s' % self.title

	@permalink
	def get_absolute_url(self):
		return ('view_post', None, {'slug': self.slug})

class Category(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)

	def __unicode__(self):
		return '%s' % self.title

	@permalink
	def get_absolute_url(self):
		return ('view_blog_category', None, {'slug': self.slug})

class Page(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	posted = models.DateField(db_index=True, auto_now_add=True)
	
	def __unicode__(self):
		return '%s' % self.title

	@permalink
	def get_absolute_url(self):
		return ('view_page', None, {'slug': self.slug})

class Technology(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True)
	description = models.TextField()
	
	def __unicode__(self):
		return self.title

	@permalink
	def get_absolute_url(self):
		return('view_tech',None, {'slug': self.slug})

class Service(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True)
	description = models.TextField()
	
	def __unicode__(self):
		return self.title

	@permalink
	def get_absolute_url(self):
		return('view_service', None, {'slug': self.slug})
