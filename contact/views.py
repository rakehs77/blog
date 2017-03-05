from django.shortcuts import render
from categories.views import categories
from profiles.views import heading
from .forms import ContactForm

# Create your views here.
def contact(request):
    form = ContactForm(request.POST or None)
    context = {'heading': heading, 'categories': categories, 'form': form}
    return render(request, 'contact.html', context)
