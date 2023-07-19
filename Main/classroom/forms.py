from django.contrib.auth.mixins import LoginRequiredMixin

from django import forms
from urllib import request
<<<<<<< HEAD
from django.db import models


from .models import Comment, Classroom, Profile


class CommentCreationForm(forms.ModelForm):

     class Meta:
         model = Comment
         fields = ['comment_text']


class StudentAddForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    
=======
from .models import Comment, Classroom, Profile, Pdf



class PdfUpload_Form(forms.ModelForm):
    class Meta:
        model = Pdf
        fields = ('title','pdflink',)
>>>>>>> origin/comment_add
