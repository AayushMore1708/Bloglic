# forms.py
from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')  # specify the fields you want to include in the form
        labels = {
            'title': 'Post Title',
            'content': 'Post Content',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)