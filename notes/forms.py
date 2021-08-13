from .models import Note
from django import forms
from django.contrib.auth.forms import UserCreationForm as UCF
from django.contrib.auth.models import User
# from colorfield.widgets import ColorWidget

class NoteForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    # color = forms.CharField(widget=forms.Select(choices=Note.COLOR_CHOICES))
    class Meta:
        model = Note
        fields = ('title','description','color')

class UserCreationForm(UCF):
    class Meta:
        fields =('username','email','password1','password2')
        model = User
        
