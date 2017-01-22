"""from .models import Post, Comment
from django import forms

class CommentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Comment
        fields = ('author', 'text', 'password')
"""