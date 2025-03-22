from django import forms
from .models import Post, Category, Tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=True)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture', 'website']

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if self.instance.pk and self.user != self.instance.author:
            raise forms.ValidationError("You don't own this post!")
        return cleaned_data
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tags']
        
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limit category choices to existing categories
        self.fields['category'].queryset = Category.objects.all()
        # Limit tag choices to existing tags
        self.fields['tags'].queryset = Tag.objects.all()
