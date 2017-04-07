"""blogger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from profiles import views as pviews
from categories import views as cviews
from blogposts import views as bpviews
from contact import views as cnviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', pviews.home, name='home'),
    url(r'^about$', pviews.about, name='about'),
    url(r'^contact$', cnviews.contact, name='contact'),
    url(r'^category/(?P<category_slug>[a-zA-Z\-]+)/$', cviews.getcategories, name='category'),
    url(r'^posts/(?P<post_id>[0-9]+)/$', bpviews.getpost, name='post'),
    url(r'^accounts/', include('allauth.urls')),
]
