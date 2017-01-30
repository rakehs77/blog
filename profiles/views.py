from django.shortcuts import render
from categories.views import categories
from .models import About
from .models import Heading
from blogposts.views import post

# Create your views here.
def home(request): 
    context = {'heading': heading, 'categories': categories, 'post': post}
    return render(request, 'home.html', context)

def about(request):
    about = About.objects.get(name='about')
    context = {'heading': heading, 'about':about, 'categories': categories}
    return render(request, 'about.html', context)

def heading():
    heading = Heading.objects.all()
    return heading

