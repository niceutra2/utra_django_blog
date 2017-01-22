from django.conf.urls import url, include
from django.contrib import admin
from blog.views import *

urlpatterns = [
   url(r'^$', PostLV.as_view(), name='index'),
   url(r'^post/(?P<slug>\w+)/$', PostDV.as_view(), name='post_detail'),
  # url(r'^post/(?P<slug>\w+)/comment/$', add_comment_to_post, name='add_comment_to_post'),
]