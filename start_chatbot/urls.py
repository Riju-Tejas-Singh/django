from django.urls import path
from . import views


urlpatterns = [
    path('start/', views.chatbot_start, name='chatbot_start'),
    path('products', views.product_list, name='products'),
    path('product/<int:pk>', views.product, name='product'),
]