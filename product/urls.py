from django.urls import path
from .views import api_products, modify_products_gui, create_product, change_product, delete_product

urlpatterns = [
    path('api/', api_products),
    path('create/', create_product.as_view()),
    path('modify/<int:id>', change_product.as_view()),
    path('delete/<int:id>', delete_product.as_view()),
    path('gui/', modify_products_gui)
]
