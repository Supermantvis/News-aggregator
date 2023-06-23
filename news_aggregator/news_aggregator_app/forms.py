from django import forms
from . import models


# class DateInput(forms.DateInput):
#     input_type = 'date'


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('content', 'user')
        widgets = {
            'user': forms.HiddenInput(),
            'created_at': forms.HiddenInput(),
        }