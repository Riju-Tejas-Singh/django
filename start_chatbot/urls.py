from django.urls import path
from . import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('start/', views.chatbot_start, name='chatbot_start'),
    path('products', views.product_list, name='products'),
    path('product/<int:pk>', views.product, name='product'),
]

urlpatterns = format_suffix_patterns(urlpatterns)