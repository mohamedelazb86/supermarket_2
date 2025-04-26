from django import forms
from blog.models import  Post,Review

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        # fields='__all__'
        fields=['title','content','image','category','draft']

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        # fields='__all__'
        fields=['review','rate']


