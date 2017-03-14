from django.forms import Form, CharField, Textarea, TextInput, CheckboxInput, PasswordInput

class SignupForm(Form):
    username = CharField(max_length=32, widget=TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Username', 'data-validation-required-message': 'Please enter your name.'}), required=True)
    email = CharField(widget=TextInput(attrs={'type': 'email','class': 'form-control', 'placeholder': 'Email address (optional)'}))
    password = CharField(widget=PasswordInput(attrs={'type': 'password','class': 'form-control', 'placeholder': 'Password', 'data-validation-required-message': 'Please enter valid password.'}), required=True)
    passwordagain = CharField(widget=PasswordInput(attrs={'type': 'password','class': 'form-control', 'placeholder': 'Password (again)', 'data-validation-required-message': 'Please enter valid password.'}), required=True)


class LoginForm(Form):
    username = CharField(max_length=32, widget=TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Username or Email', 'data-validation-required-message': 'Please enter valid username or email.'}), required=True)
    password = CharField(widget=PasswordInput(attrs={'type': 'password','class': 'form-control', 'placeholder': 'Password', 'data-validation-required-message': 'Please enter valid password.'}), required=True)
    remember = CharField(widget=CheckboxInput(attrs={'type': 'checkbox', 'class': 'checkboxinput'}))

