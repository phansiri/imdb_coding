from django import forms
from .models import Rating

STAR_RATING = [1,2,3,4,5]



class RatingForm(forms.Form):
    user_rate = forms.IntegerField(min_value=1, max_value=5)
    user_comment = forms.CharField(label='Comment', max_length=300)

    class Meta:
        model = Rating

    # class Meta:
    #     model = Rating
    #     fields = (
    #         'rate',
    #         'comment',
    #         'movie_id',
    #     )