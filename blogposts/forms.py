from django.forms import Form, CharField, Textarea, TextInput
from django.contrib.auth.models import User

class CommentForm(Form):
    user = CharField(widget=TextInput(attrs={'type': 'hidden', 'class': 'form-control'}), required=True)
    comment = CharField(widget=Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'What do you want to say?', 'data-validation-required-message': 'What do you want to say?'}), required=True)