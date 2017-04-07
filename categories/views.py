from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Category
from profiles.forms import LoginForm, SignupForm

# Create your views here.
def categories():
    categories = Category.objects.all().order_by('name')
    return categories

#display category wise
def getcategories(request, category_slug):
    category = Category.objects.get(slug__contains=category_slug)
    
    loginform = LoginForm(request.POST or None)
    if loginform.is_valid():
        login = loginform.cleaned_data.get('login')
        password = loginform.cleaned_data.get('password')

    signupform = SignupForm(request.POST or None)
    if signupform.is_valid():
        username = signupform.cleaned_data.get('username')
        email = signupform.cleaned_data.get('email')
        password1 = signupform.cleaned_data.get('password1')
        password2 = signupform.cleaned_data.get('password2')
    
    context = {'categories': categories, 'category': category, 'loginform': loginform, 'signupform': signupform}
    return render(request, 'categories.html', context)