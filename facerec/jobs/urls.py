from django.conf.urls import patterns, url
from jobs import views

urlpatterns = patterns('',
        url(r'^$', views.cameras, name='cameras'),
        )