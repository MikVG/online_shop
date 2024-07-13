from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from onlineshop.models import SalesNetwork
from onlineshop.serializers import SalesNetworkSerializer
from users.permissions import IsActiveUser


class SalesNetworkCreateAPIView(CreateAPIView):
    serializer_class = SalesNetworkSerializer
    permission_classes = (IsActiveUser,)


class SalesNetworkListAPIView(ListAPIView):
    serializer_class = SalesNetworkSerializer
    queryset = SalesNetwork.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']
    permission_classes = (IsActiveUser,)


class SalesNetworkRetrieveAPIView(RetrieveAPIView):
    serializer_class = SalesNetworkSerializer
    queryset = SalesNetwork.objects.all()
    permission_classes = (IsActiveUser,)


class SalesNetworkUpdateAPIView(UpdateAPIView):
    serializer_class = SalesNetworkSerializer
    queryset = SalesNetwork.objects.all()
    permission_classes = (IsActiveUser,)

    def perform_update(self, serializer):
        dept_field = serializer.validated_data.pop('debt')
        serializer.save()


class SalesNetworkDestroyAPIView(DestroyAPIView):
    queryset = SalesNetwork.objects.all()
    permission_classes = (IsActiveUser,)
