import base64
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from .models import CapturedImage


def capture_image(request):
    if request.method == 'POST':
        image_data = request.POST.get('imageData')
        format, imgstr = image_data.split(';base64,')
        ext = format.split('/')[-1]
        image = ContentFile(base64.b64decode(imgstr), name=f'captured_image.{ext}')

        # Save the image to the database
        captured_image = CapturedImage.objects.create(image=image)
        captured_image.save()

        return redirect('success')  # Redirect to a success page or another view

    return render(request, 'cameraapp/capture_image.html')

def success(request):
    return render(request, 'cameraapp/success.html')