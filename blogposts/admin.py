from django.contrib import admin
from .models import Post

# Register your models here.
#blog posts
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_on', 'updated_on',)
    search_fields = ('title', 'body',)
    list_filter = ('title', 'created_on', 'category')

admin.site.register(Post, PostAdmin)