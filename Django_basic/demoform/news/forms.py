from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'time_public', )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title'}),
            'content': forms.Textarea(attrs={'class': 'content'})

        }


class SendEmail(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'email_title'}))
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'email_content', 'id': 'email_id'}))
    cc = forms.BooleanField(required=False)

    
