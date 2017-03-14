from django.shortcuts import render
from .models import Post, Comment
from categories.views import categories, getcategories
from .forms import CommentForm

# Create your views here.
def posts():
    posts = Post.objects.all().order_by('-created_on')
    return posts

def getpost(request, post_id):
    post = Post.objects.get(pk=post_id)

# Comment Form
    form = CommentForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        comment = form.cleaned_data.get('comment')
        cmmnt = Comment(
            post=post,
            name=name,
            comment=comment
            )
        cmmnt.save()

    context = {'categories': categories, 'form': form, 'post': post}
    return render(request, 'post.html', context)