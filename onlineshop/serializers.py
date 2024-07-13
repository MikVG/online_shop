from rest_framework.serializers import ModelSerializer

from onlineshop.models import SalesNetwork


class SalesNetworkSerializer(ModelSerializer):

    class Meta:
        model = SalesNetwork
        fields = '__all__'
