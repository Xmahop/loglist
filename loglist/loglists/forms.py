from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django.urls import reverse

class PostForm(forms.ModelForm):
    switch_ip = forms.CharField(label='IP адрес',widget=forms.TextInput(attrs={'placeholder':'IP адрес',}))
    text = forms.CharField(label='описание',widget=forms.TextInput(attrs={'placeholder':'Описание'}))
    class Meta:
        model = Post
        fields = ['switch_ip','text']
        labels = {'': '',
                  '':''}
