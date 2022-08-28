from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Username", max_length=250, help_text='', required=True,
                                widget=forms.TextInput(attrs={"class":"form-control", "id":"username", "type":"text", "placeholder":"Username", "data-sb-validations":"required"}))
    firstname = forms.CharField(label="First Name", max_length=250, help_text='', required=True,
                                widget=forms.TextInput(attrs={"class":"form-control", "id":"firstName", "type":"text", "placeholder":"First Name", "data-sb-validations":"required"}))
    lastname = forms.CharField(label="Last Name", max_length=250, min_length=3, help_text='', required=True,
                                widget=forms.TextInput(attrs={"class":"form-control", "id":"lastName", "type":"text", "placeholder":"Last Name", "data-sb-validations":"required"}))
    email = forms.CharField(label="Email", max_length=250, min_length=5, help_text='', required=True,
                                widget=forms.TextInput(attrs={"type":"email", "class":"form-control", "id":"emailAdresse", "placeholder":"Email Adresse", "data-sb-validations":"required"}))
    password = forms.CharField(label="Password", max_length=250, min_length=8, help_text='', required=True,
                                widget=forms.TextInput(attrs={"type":"password", "class":"form-control", "id":"password", "placeholder":"Password", "data-sb-validations":"required"}))
    confirm_password = forms.CharField(label="Confirm Password", max_length=250, min_length=8, help_text='', required=True,
                                widget=forms.TextInput(attrs={"type":"password", "class":"form-control", "id":"confirm_password", "placeholder":"Confirm Password", "data-sb-validations":"required"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')