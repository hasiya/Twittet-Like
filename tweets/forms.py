from django import forms

from .models import Tweet

MAX_TWEET_LENGTH = 240


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("This Tweet is too long!")
        if len(content) < 1:
            raise forms.ValidationError("Write something to Tweet!")
        return content
