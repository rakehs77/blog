from django.shortcuts import render
from categories.views import categories
from profiles.views import heading

# Create your views here.
def contact(request):
    context = {'heading': heading, 'categories': categories}
    return render(request, 'contact.html', context)
