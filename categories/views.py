from django.shortcuts import render
from .models import Category
from blogposts.views import getpost

# Create your views here.
def categories():
    categories = Category.objects.all().order_by('name')
    return categories

#display category wise
def getcategories(request, category_name):
    getcategories = Category.objects.filter(name='Art')
    context = {'getcategories': getcategories, 'getpost':getpost}
    return render(request, 'categories.html', context)