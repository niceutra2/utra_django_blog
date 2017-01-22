from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList
#rom django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from blog.models import Post#, Comment
from django.shortcuts import render, redirect
#from blog.form import CommentForm

class PostLV(ListView) :
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDV(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

"""
    def add_comment_to_post(request, slug):
        post = get_object_or_404(Post, slug=slug)
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()
            return redirect('blog:post_detail', slug=post.slug)
        else:
            form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

    class admin:
      pass
"""


