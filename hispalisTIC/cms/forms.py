from django.forms import ModelForm
from django import forms
from cms.models import Category, Page, Post, Technology, Service

# Forms from models

class CategoryForm(ModelForm):
	class Meta:
		model = Category
  
class PostForm(ModelForm):
	class Meta:
		model = Post
 
class PageForm(ModelForm):
	class Meta:
		model = Page

class TechnologyForm(ModelForm):
	class Meta:
		model = Technology

class ServiceForm(ModelForm):
	class Meta:
		model = Service
