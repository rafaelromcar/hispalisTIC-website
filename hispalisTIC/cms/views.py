from cms.models import Page, Post, Category, Technology, Service
from cms.forms import PostForm, CategoryForm, PageForm, TechnologyForm, ServiceForm

from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# General views

def index(request):
	return render_to_response('index.html', {
		'categories': Category.objects.all(), 
		'posts': Post.objects.all()[:5]
	})

def view_post(request, slug):
	return render_to_response('view_post.html', {
		'post': get_object_or_404(Post, slug=slug)
	})

def view_category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	return render_to_response('view_category.html', {
		'category': category,
		'posts': Post.objects.filter(category=category)[:5]
	})

def view_page(request, slug):
	return render_to_response('view_page.html', {
		'page': get_object_or_404(Page, slug=slug)
	})
'''
def view_category(request, slug):
	return render_to_response('view_page.html', {
		'page': get_object_or_404(Category, slug=slug)
	})
'''
def view_service(request, slug):
	return render_to_response('view_page.html', {
		'page': get_object_or_404(Page, slug=slug)
	})


# Forms views

@login_required
def new_category_form(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('')
	else:
		form = CategoryForm()
	return render(request, "new_category.html", {'form' : form})

@login_required
def new_post_form(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('')
	else:
		form = PostForm()
	return render(request, "new_post.html", {'form' : form})

@login_required
def new_page_form(request):
	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('')
	else:
		form = PageForm()
	return render(request, "new_page.html", {'form' : form})


