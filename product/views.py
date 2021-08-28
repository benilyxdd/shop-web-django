from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import renderer_classes, api_view

from product.models import Product
from product.serializers import ProductSerializer


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def api_products(request):
    products = Product.objects.all()
    serializers = ProductSerializer(products, many=True)
    return JsonResponse(serializers.data, safe=False)
