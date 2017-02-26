from django.shortcuts import render
from .models import Post
from categories.views import categories, getcategories

# Create your views here.
def posts():
    posts = Post.objects.all().order_by('-created_on')
    return posts

def getpost(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {'categories': categories, 'post': post}
    return render(request, 'post.html', context)