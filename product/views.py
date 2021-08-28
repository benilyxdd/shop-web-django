from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from product.models import Product
from product.serializers import ProductSerializer


@api_view(['GET'])
def api_products(request):
    products = Product.objects.all()
    serializers = ProductSerializer(products, many=True)
    return JsonResponse(serializers.data, safe=False)
