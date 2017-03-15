from django.forms import Form, CharField, Textarea, TextInput

class ContactForm(Form):
    name = CharField(max_length=32, widget=TextInput(attrs={'type': 'text', 'class': 'form-control', 'id': 'name', 'name': 'name', 'placeholder': 'Name'}))
    email = CharField(max_length=32, widget=TextInput(attrs={'type': 'email', 'class': 'form-control','id': 'email', 'name': 'email', 'placeholder': 'Email'}))
    message = CharField(widget=Textarea(attrs={'class': 'form-control', 'id': 'message', 'name': 'message', 'placeholder': 'Message'}))