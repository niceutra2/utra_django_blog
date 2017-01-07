from django.views.generic import ListView


from blog.models import Post
from django.shortcuts import render, redirect
from blog.form import CommentForm
from blog.models import Post

class HomeView(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 4