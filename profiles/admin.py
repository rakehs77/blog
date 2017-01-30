from django.contrib import admin
from .models import About
from .models import Heading


# Register your models here.
#about me page
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    fields = ('description',)

admin.site.register(About, AboutAdmin)

#page headings
class HeadingAdmin(admin.ModelAdmin):
    list_display = ('pagename', 'heading', 'subheading',)

admin.site.register(Heading, HeadingAdmin)


