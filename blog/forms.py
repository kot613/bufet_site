from django import forms
from .models import Comment, NewsByEmail


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'message']
        widgets = {'name': forms.TextInput(attrs={'class': "form-control"}),
                   'message': forms.Textarea(attrs={'class': "form-control"}),
                   }


class EmailForm(forms.ModelForm):
    class Meta:
        model = NewsByEmail
        fields = ['email', ]
        widgets = {'email': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Ваш email будь ласка"})}
