from django.views.generic import ListView, DetailView
from blog.models import Post
from blog.form import CategoryForm
from django.shortcuts import render
class Post_LV(ListView) :
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
#    paginate_by = 10



def postlv(request):
    if request.method == 'POST':
       if request.POST['category'] == "Python":
           posts = Post.objects.all().filter(category='Python').order_by('-create_date')[:10]
       elif request.POST['category'] == "Etc":
           posts = Post.objects.all().filter(category='Etc').order_by('-create_date')[:10]
           print (posts)
       elif request.POST['category'] == "Django":
           posts = Post.objects.all().filter(category='Django').order_by('-create_date')[:10]
       elif request.POST['category'] == "All":
           posts = Post.objects.all().order_by('-create_date')[:10]
       form = CategoryForm()
       context = {
           "posts": posts,
           "form": form
       }
       return render(request, 'blog/post_list.html', context)
    else:
        posts = Post.objects.all().order_by('-create_date').filter(category='Dj')[:10]
        form = CategoryForm()
        context = {
            "posts": posts,
            "form": form
        }
    return render(request, 'blog/post_list.html', context)

class Post_DV(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
