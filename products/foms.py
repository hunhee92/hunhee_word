# forms.py
from django import forms
from .models import Products


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        # fields = '__all__'  # 모든 필드를 포함하고 싶은 경우
        # fields = []  # 특정 필드만 포함하고 싶은 경우
        exclude = ['likes', 'post_count']  # 특정 필드를 제외하고 싶은 경우
