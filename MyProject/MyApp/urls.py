from django.urls import path
from .views import process_bbcode

urlpatterns = [
    path('add-bbcode/', process_bbcode, name='process_bbcode'),
]
