from django.contrib import admin
from .models import Post

# Register your models here.
#blog posts
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_on', 'updated_on',)
    search_fields = ('name', 'description',)
    list_filter = ('name', 'created_on', 'category')

admin.site.register(Post, PostAdmin)