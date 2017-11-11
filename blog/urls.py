from django.conf.urls import url, include
from django.contrib import admin
from blog.views import *
from django.conf.urls.static import static
from my_blog import settings

urlpatterns = [
   url(r'^$', postlv, name='index'),
   url(r'^(?P<slug>\w+)/$', Post_DV.as_view(), name='post_detail'),
]
