from django.forms import Form, CharField, Textarea, TextInput

class ContactForm(Form):
    fullname = CharField(max_length=32, widget=TextInput(attrs={'type': 'text', 'class': 'form-control', 'id': 'name', 'placeholder': 'Fullname', 'data-validation-required-message': 'Please enter your name.'}), required=True)
    email = CharField(max_length=32, widget=TextInput(attrs={'type': 'email', 'class': 'form-control', 'id': 'email', 'placeholder': 'Email', 'data-validation-required-message': 'Please enter your email.'}), required=True)
    message = CharField(widget=Textarea(attrs={'class': 'form-control', 'id': 'message', 'placeholder': 'Message', 'data-validation-required-message': 'Please write your message.'}), required=True)