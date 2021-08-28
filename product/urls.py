from django.urls import path
from .views import api_products

urlpatterns = [
    path('api/', api_products)
]
