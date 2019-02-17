from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.person_list, name='person_list'),
    url(r'^person/(?P<pk>\d+)/$', views.person_detail, name='person_detail'),
    url(r'^person/new/$', views.person_new, name='person_new'),
    url(r'^person/(?P<pk>\d+)/edit/$', views.person_edit, name='person_edit'),
    url(r'^person/(?P<pk>\d+)/event/new/$', views.event_new, name='event_new'),
    url(r'^person/(?P<pk>\d+)/event/(?P<ek>\d+)/edit/$', views.event_edit, name='event_edit'),
]
