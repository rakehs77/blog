from django.shortcuts import render
from categories.views import categories
from .models import About
from .models import Heading
from blogposts.views import posts
from .forms import LoginForm, SignupForm


# Create your views here.
def home(request): 

    
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

    context = {'heading': heading, 'categories': categories, 'posts': posts, 'loginform': loginform, 'signupform': signupform}
    return render(request, 'home.html', context)

def about(request):
    about = About.objects.get(name='about')
    context = {'heading': heading, 'about':about, 'categories': categories}
    return render(request, 'about.html', context)

def heading():
    heading = Heading.objects.all()
    return heading

def profile():
    user = request.user
    return user


