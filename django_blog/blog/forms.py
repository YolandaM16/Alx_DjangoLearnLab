from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms
from django import Comment

#class CustomUserCreationForm(UserCreationForm):
#   email = forms.EmailField(required=True)

#   class Meta:
#       model = User
#        fields = ["username", "email", "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "profile_pic"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
