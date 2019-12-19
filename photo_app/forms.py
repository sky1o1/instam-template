from django import forms
from .models import PhotoModel,CommentModel

class PhotoForm(forms.ModelForm):
    class Meta:
        model = PhotoModel
        fields = '__all__'
        #fields = ()'photo','comment') #for specific

class CommentForm(forms.ModelForm):
    class meta:
        model = CommentModel
        fields = '__all__'
