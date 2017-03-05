from django.forms import Form, CharField, Textarea, TextInput

class ContactForm(Form):
    fullname = CharField(max_length=32, widget=TextInput(attrs={'type': 'text', 'class': 'form-control', 'id': 'name'}), required=True)
    email = CharField(max_length=32, widget=TextInput(attrs={'type': 'email', 'class': 'form-control', 'id': 'email'}), required=True)
    message = CharField(widget=Textarea(attrs={'class': 'form-control', 'id': 'message'}), required=True)