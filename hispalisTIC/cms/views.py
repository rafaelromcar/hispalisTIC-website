from cms.models import Page, Post, Category, CategoryForm, PostForm, PageForm

from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect

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

# Forms views
	
def new_category_form(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('')
	else:
		form = CategoryForm()
	return render(request, "new_category.html", {'form' : form})

def new_post_form(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('')
	else:
		form = PostForm()
	return render(request, "new_post.html", {'form' : form})

def new_page_form(request):
	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('')
	else:
		form = PageForm()
	return render(request, "new_page.html", {'form' : form})

def new_menu_form(request):
	if request.method == 'POST':
		form = MenuForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpReponseRedirect('')
	else:
		form = MenuForm()
	return render(request, "new_menu.html", {'form' : form})
