from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.routers import DefaultRouter

from users.models import User
from users.serializers import UserSerializer

class UserViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, \
                  mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    '''
    Viewset for User Model
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = DefaultRouter()
router.register("users", UserViewSet, "user")