from django.db import models
from django.contrib.auth.models import User
from django import forms

class UserForm(ModelForm):
	class Meta:
		model = User 
