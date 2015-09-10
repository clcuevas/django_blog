from django.conf.urls import url
# Import the views file from root dir (.)
from . import views

urlpatterns = [
  url(r'^$', views.post_list, name='post_list'),
  # The URL should contain the word post and /
  # The URL will then transfer a pk variable to the view, pk = primary key
  # The pk variable can only be a number between [0-9] with one or more digits (+)
  url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
  url(r'^post/new/$', views.post_new, name='post_new'),
  url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
