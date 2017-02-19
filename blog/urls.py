from django.conf.urls import url, include
from django.contrib import admin
from blog.views import *

urlpatterns = [
   url(r'^$', PostLV.as_view(), name='index'),
   url(r'^(?P<slug>\w+)/$', Post_DV.as_view(), name='post_detail'),
]