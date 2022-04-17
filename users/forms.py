
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from neighbourhood.models import Profile

#update profile email and username
class UserRegistrationForm(UserCreationForm):
    '''
    Form that inherits from the django UserCreationForm and adds email field 
    '''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    '''
    Form that inherits from the django ModelForm and allows user to update their profile
    '''

    class Meta:
        model = Profile
        fields = ['profile_photo', 'bio']
