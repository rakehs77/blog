from django.shortcuts import render
from .models import Post, Comment
from categories.views import categories, getcategories
from .forms import CommentForm
from django.contrib.auth.models import User


# Create your views here.
def posts():
    posts = Post.objects.all().order_by('-created_on')
    return posts

def getpost(request, post_id):
    post = Post.objects.get(pk=post_id)

# Comment Form
    
    form = CommentForm(request.POST or None, initial={'user': request.user.id})
    # form.user = request.user.id
    if form.is_valid():
        comment = form.cleaned_data.get('comment')
        user_id = form.cleaned_data.get('user')
        user = User.objects.get(pk=user_id)
        cmmnt = Comment(
            post=post,
            user=user,
            comment=comment
            )
        cmmnt.save()

    context = {'categories': categories, 'form': form, 'post': post}
    return render(request, 'post.html', context)