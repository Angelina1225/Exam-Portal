from django import forms
from .models import std_data

class RegisterForm(forms.ModelForm):
    username = forms.CharField(required=False)
    email = forms.CharField(required=True)
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    password1 = forms.CharField(min_length=8, label=("Password"), strip=False, widget=forms.PasswordInput())
    password2 = forms.CharField(label=("Confirm Password"), strip=False, widget=forms.PasswordInput())

    class Meta:
        model = std_data
        fields = ['username', 'email', 'firstname', 'lastname', 'password1', 'password2']
    
    
    def clean_email(self):
        if std_data.objects.filter(email__iexact=self.data['email']).exists():
            raise forms.ValidationError('This email is already registered')
        return self.data['email']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['icon_name'] = "fa fa-envelope"
        self.fields['username'].widget.attrs['icon_name'] = "fa fa-id-card"
        self.fields['firstname'].widget.attrs['icon_name'] = "fa fa-id-card"
        self.fields['lastname'].widget.attrs['icon_name'] = "fa fa-id-card"
        self.fields['password1'].widget.attrs['icon_name'] = "fa fa-lock"
        self.fields['password2'].widget.attrs['icon_name'] = "fa fa-lock"