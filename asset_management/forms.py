# asset_management/forms.py

from django import forms
from .models import Device


class AssetForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'condition', 'company', 'checked_out']
