from django.forms import Form, CharField, Textarea, TextInput, CheckboxInput, PasswordInput

class SignupForm(Form):
    username = CharField(max_length=15, widget=TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Username'}))
    email = CharField(widget=TextInput(attrs={'type': 'email','class': 'form-control', 'placeholder': 'Email address (optional)'}))
    password1 = CharField(widget=PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'placeholder': 'Password'}))
    password2 = CharField(widget=PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'placeholder': 'Password (again)'}))


class LoginForm(Form):
    login = CharField(max_length=32, widget=TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Username or Email'}), required=True)
    password = CharField(widget=PasswordInput(attrs={'type': 'password','class': 'form-control', 'placeholder': 'Password'}), required=True)
    remember = CharField(widget=CheckboxInput(attrs={'type': 'checkbox', 'class': 'checkboxinput'}))

