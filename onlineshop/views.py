from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from onlineshop.models import SalesNetwork
from onlineshop.serializers import SalesNetworkSerializer


class SalesNetworkCreateAPIView(CreateAPIView):
    serializer_class = SalesNetworkSerializer


class SalesNetworkListAPIView(ListAPIView):
    serializer_class = SalesNetworkSerializer
    queryset = SalesNetwork.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']


class SalesNetworkRetrieveAPIView(RetrieveAPIView):
    serializer_class = SalesNetworkSerializer
    queryset = SalesNetwork.objects.all()


class SalesNetworkUpdateAPIView(UpdateAPIView):
    serializer_class = SalesNetworkSerializer
    queryset = SalesNetwork.objects.all()

    def perform_update(self, serializer):
        dept_field = serializer.validated_data.pop('debt')
        serializer.save()


class SalesNetworkDestroyAPIView(DestroyAPIView):
    queryset = SalesNetwork.objects.all()
