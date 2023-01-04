
from django.urls import path
from .views import home , movies






urlpatterns = [
   
    path('',  home),
    path('home/',  home),
    path('movies/',  movies),
    

]
