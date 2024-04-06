from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.routers import DefaultRouter

from users.models import User, UserGroup
from users.serializers import UserSerializer, UserGroupSerializer

class UserViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, \
                  mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    '''
    Viewset for User Model
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserGroupViewset(mixins.ListModelMixin, mixins.CreateModelMixin, \
                       mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    '''
    Viewset for UserGroup Model
    '''
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer

router = DefaultRouter()
router.register("users", UserViewSet, "user")
router.register("groups", UserGroupViewset, "group")