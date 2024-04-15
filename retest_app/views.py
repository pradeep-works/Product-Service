from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.routers import DefaultRouter

from retest_app.models import Product
from retest_app.serializers import ProductSerializer
from retest_app.permissions import AllowAdminOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

class ProductViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,\
                     mixins.UpdateModelMixin, GenericViewSet):
    '''
    Viewset for Product model
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['price', 'name']
    ordering_fields = ['price']
    search_fields = ['name', 'display_name']
 
    def get_serializer_class(self):
        return super().get_serializer_class()

router = DefaultRouter()
router.register("product", ProductViewSet, "product")