from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^post/new/$', views.post_new, name='post_new'),
    #url(r'^choseninterest/$', views.choseninterest, name='choseninterest'),
    url(r'^userProfiles/edit/$', views.edit_userinfo, name='edit_userinfo'),
    url(r'^change-password/$', views.change_password, name='change_password'),
]
