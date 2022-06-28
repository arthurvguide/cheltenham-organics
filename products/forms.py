from django.forms import ModelForm

from .models import Review


class ReviewForm(ModelForm):
    """
    Form for users to review products.
    """
    class Meta:
        model = Review
        fields = (
            'title',
            'review_subject',
        )
