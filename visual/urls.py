# Create your views here.
from django.conf.urls import patterns, url

from visual import views

urlpatterns = patterns('',
		url(r'^index$', views.index, name='index')
)
