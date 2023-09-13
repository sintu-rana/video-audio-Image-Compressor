from django.urls import path
from app.views import *

#URLs-

urlpatterns = [
    path('home/', view_home),
    path('video-compression/', video_compression, name='video_compression'),
    path('audio-compression/', audio_compression, name='audio_compression'),
    path('image-compression/', image_compression, name='image_compression'),
   
]
