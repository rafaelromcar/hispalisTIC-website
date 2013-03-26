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
	category = models.ForeignKey('cms.Category')

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
	
	menus = models.ManyToManyField('cms.Menu')

	def __unicode__(self):
		return '%s' % self.title

	@permalink
	def get_absolute_url(self):
		return ('view_page', None, {'slug': self.slug})

class Menu(models.Model):
	title = models.CharField(max_length=100)

# Forms

class CategoryForm(ModelForm):
	class Meta:
		model = Category

class PostForm(ModelForm):
	class Meta:
		model = Post

class PageForm(ModelForm):
	class Meta:
		model = Page

class MenuForm(ModelForm):
	class Meta:
		model = Menu
