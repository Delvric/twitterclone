from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
