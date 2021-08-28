from json import load
from re import template
from django.http.response import HttpResponse, JsonResponse
from django.core import serializers
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework import mixins, generics

from product.models import Product
from product.serializers import ProductSerializer


@api_view(['GET'])
def api_products(request):
    products = Product.objects.all()
    serializers = ProductSerializer(products, many=True)
    return JsonResponse(serializers.data, safe=False)


def modify_products_gui(request):
    products = Product.objects.all()
    template = loader.get_template('product/index.html')
    context = {
        'products': products
    }
    return HttpResponse(template.render(context, request))


class create_product(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = ProductSerializer

    def post(self, request):
        return self.create(request)


class change_product(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'

    def put(self, request, id):
        return self.update(request, id)


class delete_product(generics.GenericAPIView, mixins.DestroyModelMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'

    def delete(self, request, id):
        return self.destroy(request, id)
