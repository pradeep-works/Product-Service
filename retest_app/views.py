from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.routers import DefaultRouter

from retest_app.models import Product
from retest_app.serializers import ProductSerializer
from retest_app.permissions import AllowAdminOnly

class ProductViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,\
                     mixins.UpdateModelMixin, GenericViewSet):
    '''
    Viewset for Product model
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method.upper() in ['HEAD', 'OPTIONS']:
            return []
        if self.request.method.upper() in ['GET']:
            return [IsAuthenticated()]
        if self.request.method.upper() in ['POST', 'PATCH', 'PUT', 'DELETE']:
            return [AllowAdminOnly()]
    
    def get_serializer_class(self):
        return super().get_serializer_class()

router = DefaultRouter()
router.register("product", ProductViewSet, "product")