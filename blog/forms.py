from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'message']
        widgets = {'name': forms.TextInput(attrs={'class': "form-control"}),
                   'message': forms.Textarea(attrs={'class': "form-control"}),
                   }
