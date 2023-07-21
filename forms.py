# forms.py
from django import forms

class UserRegistrationForm(forms.Form):
    firstname = forms.CharField(max_length=50, label='First Name', required=True)
    surname = forms.CharField(max_length=50, label='Surname', required=True)
    username = forms.CharField(max_length=150, label='Username', required=True)
    email = forms.EmailField(max_length=254, label='Email', required=True)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password', required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match. Please try again.")
