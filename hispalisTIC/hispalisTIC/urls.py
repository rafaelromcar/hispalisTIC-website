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
	url(r'^blog/post/(?P<slug>[^\.]+)/', 'cms.views.view_post',	name='view_post'),
	url(r'^blog/category/(?P<slug>[^\.]+)/', 'cms.views.view_category', name='view_category'),
	url(r'^page/(?P<slug>[^\.]+)/', 'cms.views.view_page', name='page'),
	url(r'technologies/', 'cms.views.index', name = 'technologies'),
	url(r'services/', 'cms.views.index', name = 'services'),
	url(r'services/(?P<slug>[^\.]+)/', 'cms.views.view_page', name='service'),
	
	# Contact form
	url(r'^$', 'cms.views.index', name='contact'),

	# CMS app - forms url
	url(r'^blog/new_post/', 'cms.views.new_post_form', name='new_post'),
	url(r'^blog/new_category/', 'cms.views.new_category_form', name='new_category'),
	url(r'^page/new_page/', 'cms.views.new_page_form', name='new_page')
)
