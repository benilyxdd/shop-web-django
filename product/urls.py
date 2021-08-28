from django.urls import path
from .views import api_products, create_product

urlpatterns = [
    path('api/', api_products),
    path('create/', create_product.as_view())
]
