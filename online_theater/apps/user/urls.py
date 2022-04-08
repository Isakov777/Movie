from django.urls import path
from apps.movie.views import video


urlpatterns = [
    path('video/', video, name = 'videos'),
]