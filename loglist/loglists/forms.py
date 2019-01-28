from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django.urls import reverse

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['switch_ip','text']
        labels = {'': '',
                  '':''}
