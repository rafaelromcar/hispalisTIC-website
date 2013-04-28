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

	# Index & other
	url(r'^$', 'cms.views.index', name='home'),

	# CMS app
	url(r'^blog/new_post/', 'cms.views.new_post_form', name='new_post'),
	url(r'^blog/new_category/', 'cms.views.new_category_form', name='new_category'),
	url(r'^blog/post/(?P<slug>[^\.]+)/', 'cms.views.view_post',	name='view_post'),
	url(r'^blog/posts/', 'cms.views.posts',	name='view__all_posts'),
	url(r'^blog/category/(?P<slug>[^\.]+)/', 'cms.views.view_category', name='view_category'),
	url(r'^blog/categories/', 'cms.views.categories', name='view_all_categories'),
	url(r'^blog/$', 'cms.views.blog',	name='blog'),
	url(r'^page/new_page/', 'cms.views.new_page_form', name='new_page'),
	url(r'^page/(?P<slug>[^\.]+)/', 'cms.views.view_page', name='view_page'),
	url(r'^technologies/$', 'cms.views.technologies', name = 'technologies'),
	url(r'^technologies/new_technology/', 'cms.views.new_technology_form', name='new_technology'),
	url(r'^services/new_service/', 'cms.views.new_service_form', name='new_service'),
	url(r'^services/(?P<slug>[^\.]+)/', 'cms.views.view_service', name='view_service'),
	url(r'^services/$', 'cms.views.services', name = 'services'),

	
	# Contact form
	url(r'^$', 'cms.views.index', name='contact')

)
