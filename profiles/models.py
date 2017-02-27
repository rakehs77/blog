from django.db import models
from categories.models import Category

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(default="Write something about yourself. HTML allowed")

    def __str__(self):
        return self.pagename

    def __repr__(self):
        return self.name

class Heading(models.Model):
    pagename = models.CharField(max_length=32, editable=False)
    heading = models.CharField(max_length=32)
    subheading = models.CharField(max_length=120)



    def __str__(self):
        return self.pagename

    def __repr__(self):
        return self.name