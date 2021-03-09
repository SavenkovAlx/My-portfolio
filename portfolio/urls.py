from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('projects/', projects, name='projects'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
