from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name