from django.contrib import admin
from models import Post, Category

class PostAdmin(admin.ModelAdmin):
	exclude = ['posted']
	prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post)
admin.site.register(Category)
