from django import forms
from django.utils.translation import gettext_lazy as _
from cart.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'title_en',
            'slug_en',
            'short_product_detail_en',
            'product_detail_en',
            'featured',
            'available_colours',
            'available_sizes',
            'primary_category',
            'secondary_categories',
            'title_fr',
            'slug_fr',
            'short_product_detail_fr',
            'product_detail_fr',
        )
