from django.urls import path
from .views import chatbot_start

urlpatterns = [
    path('start/', chatbot_start, name='chatbot_start'),
]