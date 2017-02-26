from django.contrib import admin
from .models import Category

# Register your models here.
#category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug',)
    search_fields = ('name',)

    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)