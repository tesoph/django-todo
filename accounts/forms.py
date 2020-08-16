from django import forms

class UserLoginForm(forms.Form):
    """Form to be used to login user"""
    
    username = forms.CharField()
    ##tells django we want to render a normal text input box but we want it to be of type "password"
    password = forms.CharField(widget=forms.PasswordInput)
