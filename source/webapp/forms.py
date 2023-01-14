from django import forms
from webapp.models import Product, Review
from django.forms import widgets


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'image')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'product', 'review_text', 'rating']
        widgets = {
            'author': widgets.Select(attrs={'placeholder': 'Автор'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['author'].widget = forms.HiddenInput()
        # self.fields['product'].widget = forms.HiddenInput()
        self.fields['rating'].widget = forms.NumberInput(attrs={'min': 1, 'max': 5})
