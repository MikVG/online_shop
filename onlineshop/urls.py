from django.urls import path

from onlineshop.apps import OnlineshopConfig
from onlineshop.views import SalesNetworkCreateAPIView, SalesNetworkListAPIView, SalesNetworkRetrieveAPIView, \
    SalesNetworkUpdateAPIView, SalesNetworkDestroyAPIView

app_name = OnlineshopConfig.name

urlpatterns = [
    path('', SalesNetworkListAPIView.as_view(), name='list'),
    path('create/', SalesNetworkCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', SalesNetworkRetrieveAPIView.as_view(), name='detail'),
    path('update/<int:pk>/', SalesNetworkUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>/', SalesNetworkDestroyAPIView.as_view(), name='delete'),
]
