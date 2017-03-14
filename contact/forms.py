from django.forms import Form, CharField, Textarea, TextInput

class ContactForm(Form):
    name = CharField(max_length=32, widget=TextInput(attrs={'type': 'text', 'class': 'form-control','id': 'name', 'placeholder': 'Name', 'data-validation-required-message': 'Please enter your name.'}), required=True)
    email = CharField(max_length=32, widget=TextInput(attrs={'type': 'email', 'class': 'form-control','id': 'email', 'placeholder': 'Email', 'data-validation-required-message': 'Please enter your email.'}), required=True)
    message = CharField(widget=Textarea(attrs={'class': 'form-control', 'id': 'message', 'placeholder': 'Message', 'data-validation-required-message': 'What do you want to say?'}), required=True)