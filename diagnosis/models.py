from django.db import models
from django import forms


## this will be used to take in the images that can be processed when we add the image to the selection
class XRayImage(models.Model):
    image = models.ImageField(upload_to='xray_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class XRayImageForm(forms.ModelForm):
    class Meta:
        model = XRayImage
        fields = ['image']


