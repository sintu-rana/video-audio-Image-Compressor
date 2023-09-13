# compression/models.py
from django.db import models

class CompressedVideo(models.Model):
    video_file = models.FileField(upload_to='compressed_videos/')
    # Add other fields as needed

class CompressedAudio(models.Model):
    audio_file = models.FileField(upload_to='compressed_audio/')
    # Add other fields as needed

class CompressedImage(models.Model):
    image_file = models.ImageField(upload_to='compressed_images/')
    # Add other fields as needed