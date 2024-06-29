from django import forms
from django.core import validators

from firstapp import models


class MusicianForm(forms.ModelForm):

    class Meta:
        model = models.Musician
        
        fields = "__all__"
        



class AlbumbForm(forms.ModelForm):
    relase_date  = forms.DateField(widget= forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = models.Album
        fields = "__all__"
    