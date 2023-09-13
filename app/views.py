from django.shortcuts import render, redirect
from django.core.files.base import ContentFile  # Import ContentFile
import ffmpeg
from django.http import HttpResponse
from pydub import AudioSegment
from PIL import Image



# Create your views here.

def view_home(request):
    resp=render(request, 'app/home.html')
    return resp

## video compression

def video_compression(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['video_file']
        output_file = 'compressed_video.mp4'  # Specify the output file name and format

        # Input and output paths
        input_path = f'media/{uploaded_file.name}'
        output_path = f'media/{output_file}'

        # Save the uploaded video to a temporary file
        with open(input_path, 'wb') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Video compression using FFmpeg
        try:
            ffmpeg.input(input_path).output(output_path, vf='scale=640:480').run()
        except ffmpeg.Error as e:
            return HttpResponse(f"Video compression failed: {e.stderr}", status=500)

        return HttpResponse(f"Video compression successful. <a href='{output_path}'>Download</a>")

    return render(request, 'app/video_compression.html')


## 2. Audio Compression:


def audio_compression(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['audio_file']
        output_file = 'compressed_audio.mp3'  # Specify the output file name and format

        # Input and output paths
        input_path = f'media/{uploaded_file.name}'
        output_path = f'media/{output_file}'

        # Save the uploaded audio to a temporary file
        with open(input_path, 'wb') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Audio compression using pydub
        try:
            audio = AudioSegment.from_file(input_path)
            audio.export(output_path, format='mp3', bitrate='64k')  # Adjust the bitrate as needed
        except Exception as e:
            return HttpResponse(f"Audio compression failed: {str(e)}", status=500)

        return HttpResponse(f"Audio compression successful. <a href='{output_path}'>Download</a>")

    return render(request, 'app/audio_compression.html')


### Image compression


def image_compression(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image_file']
        output_file = 'compressed_image.jpg'  # Specify the output file name and format

        # Input and output paths
        input_path = f'media/{uploaded_file.name}'
        output_path = f'media/{output_file}'

        # Save the uploaded image to a temporary file
        with open(input_path, 'wb') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Image compression using Pillow
        try:
            image = Image.open(input_path)
            image.thumbnail((640, 480))  # Resize the image to fit within 640x480 pixels
            image.save(output_path, 'JPEG', quality=80)  # Adjust the quality as needed
        except Exception as e:
            return HttpResponse(f"Image compression failed: {str(e)}", status=500)

        return HttpResponse(f"Image compression successful. <a href='{output_path}'>Download</a>")

    return render(request, 'app/image_compression.html')

