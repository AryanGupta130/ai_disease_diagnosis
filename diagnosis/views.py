# diagnosis/views.py

from django.shortcuts import render

# Home page view
def index(request):
    return render(request, 'diagnosis/index.html')

# Image upload page view
def upload_image(request):
    if request.method == 'POST':
        # Handle image upload logic here
        pass
    return render(request, 'diagnosis/upload_image.html')
