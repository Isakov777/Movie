from django import forms
from .models import Review, Rating, RatingStar, SeriesReview, CartoonReview,  AnimeReiview

class ReviewForm(forms.ModelForm):
    """Форма отзыва"""
    class Meta:
        model = Review
        fields = ('name', 'email', 'text')



class SeriesReviewForm(forms.ModelForm):
    """Форма отзыва"""
    class Meta:
        model = SeriesReview
        fields = ('name', 'email', 'text')



class CartoonReviewForm(forms.ModelForm):
    """Форма отзыва"""
    class Meta:
        model = CartoonReview
        fields = ('name', 'email', 'text')




class AnimeReviewForm(forms.ModelForm):
    """Форма отзыва"""
    class Meta:
        model = AnimeReiview
        fields = ('name', 'email', 'text')


class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(
        queryset = RatingStar.objects.all(), widget = forms.RadioSelect(), empty_label = None
    )

    class Meta:
        model = Rating
        fields = ('star',)