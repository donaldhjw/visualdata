from django.conf.urls import patterns, include, url
import os

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'visualdata.views.home', name='home'),
    # url(r'^visualdata/', include('visualdata.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url(r'^visual/', include('visual.urls')),
	url(r'^template/vestibule/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.dirname(os.path.abspath(__file__)) + '/../template/vestibule/'}),
)
