from django import forms
from .models import Rating

STAR_RATING = [1,2,3,4,5]


class RatingForm(forms.Form):
    user_rate = forms.CharField(
        widget=forms.Select(choices=STAR_RATING),
    )
    user_comment = forms.CharField(max_length=300)
    user_movie = forms.ChoiceField()


    # class Meta:
    #     model = Rating
    #     fields = [
    #         'rate',
    #         'comment',
    #         'movie_id',
    #     ]