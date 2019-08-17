from django import forms
from .models import Rating


class RatingForm(forms.Form):
    user_rate = forms.IntegerField(min_value=1, max_value=5)
    user_comment = forms.CharField(label='Comment', max_length=300)

    class Meta:
        model = Rating
