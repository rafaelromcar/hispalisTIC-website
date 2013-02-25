from blog.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
	return render_to_response('index.html', {
		'categories': Category.objects.all(), 
		'posts': Blog.objects.all()[:5]
	})

def view_post(request, slug):
	return render_to_response('view_post.html', {
		'post': get_object_or_404(Blog, slug=slug)
	})

def view_category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	return render_to_response('view_category.html', {
		'category': category,
		'posts': Blog.objects.filter(category=category)[:5]
	})

# Forms views

def new_category_form(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('')
	else:
		form = new_category_form(request)
	return render(request, 'new_category.html', {'form': form})        
