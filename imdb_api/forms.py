from django import forms
from .models import Rating

# Class that inherits from forms.Form.
# This is another form of validation on the backend that does not involve the rest api
class RatingForm(forms.Form):
    user_rate = forms.IntegerField(min_value=1, max_value=5)
    user_comment = forms.CharField(label='Comment', max_length=300)

    class Meta:
        model = Rating
