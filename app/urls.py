from django.urls import path
from app.views import *

#URLs-

urlpatterns = [
    path('home/', view_home),
]
