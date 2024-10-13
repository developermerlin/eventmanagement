# forms.py
from django import forms


class CustomRegistrationForm(forms.Form):
    firstname = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lastname = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    contact = forms.CharField(
        max_length=15,  # Adjust as needed, e.g., for international formats
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'type': 'tel'})
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))  # Added email field
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))