from tensorflow.keras.models import load_model  # Correct import for load_model
from tensorflow.keras.preprocessing import image  # Correct import for image processing

from django.shortcuts import render
from django.conf import settings
import os
from .models import XRayImageForm  # This should be from .forms not .models
import numpy as np

# Home page view
def index(request):
    return render(request, 'diagnosis/index.html')

def about_tb(request):
    return render(request, 'diagnosis/about_tb.html')

# Image upload page view
def upload_image(request):
    if request.method == 'POST':
        pass  # Image upload logic here
    return render(request, 'diagnosis/upload_image.html')



model = load_model(os.path.join(settings.BASE_DIR, 'tb_model.h5'))

def upload_xray(request):
    if request.method == 'POST':
        form = XRayImageForm(request.POST, request.FILES)
        if form.is_valid():
            xray_image = form.save()

            # Get path to the uploaded image
            image_path = os.path.join(settings.MEDIA_ROOT, xray_image.image.name)

            # Preprocess and predict
            img = image.load_img(image_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)

            # Make the prediction
            prediction = model.predict(img_array)
            result = 'Positive for TB' if prediction[0][0] > 0.5 else 'Negative for TB'

            return render(request, 'diagnosis/result.html', {'result': result})

    else:
        form = XRayImageForm()

    return render(request, 'diagnosis/upload.html', {'form': form})
