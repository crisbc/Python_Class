from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.index, name='matchedUsers'),
    url(r'^sendRequest$', views.sendRequest, name='sendRequest'),
]
