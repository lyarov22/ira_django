from django import forms
from .models import Week

class WeekForm(forms.ModelForm):
    class Meta:
        model = Week
        fields = '__all__'  # Или укажите только нужные поля
