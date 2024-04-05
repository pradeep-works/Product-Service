from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework.routers import DefaultRouter

from retest_app.models import Product
from retest_app.serializers import ProductSerializer

class ProductViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,\
                     mixins.UpdateModelMixin, GenericViewSet):
    '''
    Viewset for Product model
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

router = DefaultRouter()
router.register("product", ProductViewSet, "product")