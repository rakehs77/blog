from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Category

# Create your views here.
def categories():
    categories = Category.objects.all().order_by('name')
    return categories

#display category wise
def getcategories(request, category_slug):
    category = Category.objects.get(slug__contains=category_slug)

    # try:
    #     category = Category.objects.get(name=category_name)
    # except Category.DoesNotExist:
    #     raise Http404("Resource not found")

    #categories = Category.objects.filter(name__like='art')
    #if not categories:
    #   pass

    # select * from categories where name='art'
    # Category.objects.get(name='art') => select * from categories where name='art'
    # Category.objects.filter(name__like='art') => select * from categories where name like '%art%'

    # Category.objects.filter(get_product_filter())
    
    context = {'categories': categories, 'category': category}
    return render(request, 'categories.html', context)