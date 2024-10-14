from django import forms
from .models import XRayImage

class XRayImageForm(forms.ModelForm):
    class Meta:
        model = XRayImage
        fields = ['image']
