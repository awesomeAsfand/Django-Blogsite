from django.forms import ModelForm, forms
from .models import Comments


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('comment_text',)

