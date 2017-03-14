from django.db import models
from categories.models import Category

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=32)
    tagline = models.CharField(max_length=50, blank=True, default="Write a brief detail or leave empty.")
    body = models.TextField(default="HTML allowed.")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, null=False, blank=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=32)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, null=False, blank=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name