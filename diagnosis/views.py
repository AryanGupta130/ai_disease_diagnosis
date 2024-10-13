# diagnosis/views.py

from django.shortcuts import render

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
