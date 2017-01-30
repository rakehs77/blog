from django.db import models
from categories.models import Category

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, null=False, blank=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name