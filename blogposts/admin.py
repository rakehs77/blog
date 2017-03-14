from django.contrib import admin
from .models import Post, Comment


# Register your models here.
#blog posts
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_on', 'updated_on',)
    search_fields = ('title', 'body',)
    list_filter = ('title', 'created_on', 'category')

admin.site.register(Post, PostAdmin)

# comments
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'comment', 'created_on', 'updated_on',)
    search_fields = ('name', 'post',)
    list_filter = ( 'post', 'created_on')

admin.site.register(Comment, CommentAdmin)