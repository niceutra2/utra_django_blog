from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList
#rom django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from blog.models import Post
from django.shortcuts import render, redirect





class PostLV(ListView) :
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDV(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
