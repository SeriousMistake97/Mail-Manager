
from django import forms
from blog.models import Blog
from client.forms import StyleFormMixin


class BlogForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'content', 'preview',)
