from django import forms
from .models import Post

# class PostForm(forms.Form):
#     title = forms.CharField(max_length=20)
#     contents = forms.CharField()
#     main_image = forms.ImageField(required=False)



class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title", "contents", "main_image")