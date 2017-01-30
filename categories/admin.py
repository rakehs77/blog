from django.contrib import admin
from .models import Category

# Register your models here.
#category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)