from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.Form):
    username = forms.CharField()
    display_name = forms.CharField()
    age = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)