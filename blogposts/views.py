from django.shortcuts import render
from .models import Post

# Create your views here.
def post():
    post = Post.objects.all().order_by('-created_on')
    return post

def getpost():
    getpost = Post.objects.get(category='category_name')
    return getpost

def posts(request):
    
    return (request, 'post.html', {'post': post})