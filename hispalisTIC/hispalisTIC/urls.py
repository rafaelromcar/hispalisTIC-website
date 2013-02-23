from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hispalisTIC.views.home', name='home'),
    # url(r'^hispalisTIC/', include('hispalisTIC.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

	# Blog app
	url(r'^$', 'blog.views.index'),
	url(r'^blog/view/(?P<slug>[^\.]+).html', 
    	'hispalisTIC.blog.views.view_post', 
    	name='view_blog_post'),
	url(r'^blog/category/(?P<slug>[^\.]+).html', 
    	'hispalisTIC.blog.views.view_category', 
    	name='view_blog_category')
)
