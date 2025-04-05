from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import MaxLengthValidator

class ExtendedRegisterForm(UserCreationForm):
    # password1 = forms.CharField(label='First Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Conform Password Again',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email': 'Email ID','username':'User_name'}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].required = True
        self.fields['first_name'].validators.append(MaxLengthValidator(10, message="First name must not exceed 10 characters."))
        self.fields['last_name'].required = True

class ExtendedUpdateProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','last_login']
        labels = {'email': 'Email ID','username':'User_name'}