from django import forms
from blog.models import Post

class CategoryForm(forms.Form):
    MY_CHOICES = (
        ('All', 'All'),
        ('Django', 'Django'),
        ('Python', 'Python'),
        ('Etc', 'Etc')
    )
    category = forms.ChoiceField(widget=forms.Select, choices=MY_CHOICES)
