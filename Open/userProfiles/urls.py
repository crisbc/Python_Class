from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^post/new/$', views.post_new, name='post_new'),
    #url(r'^choseninterest/$', views.choseninterest, name='choseninterest'),
    url(r'^edit_userinfo/$', views.edit_userinfo, name='edit_userinfo'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^other_users/$', views.other_users, name='other_users'),
    url(r'^other_users/(?P<pk>\d+)/$', views.other_users, name='other_users_with_pk'),
]
