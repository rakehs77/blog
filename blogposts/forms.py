from django.forms import Form, CharField, Textarea, TextInput

class CommentForm(Form):
    name = CharField(max_length=32, widget=TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Name', 'data-validation-required-message': 'Please enter your name.'}), required=True)
    comment = CharField(widget=Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'What do you want to say?', 'data-validation-required-message': 'What do you want to say?'}), required=True)