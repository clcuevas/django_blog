from django.conf.urls import url
# Import the views file from root dir (.)
from . import views

urlpatterns = [
  url(r'^$', views.post_list, name='post_list')
]
