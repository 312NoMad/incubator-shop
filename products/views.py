from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter, NumberFilter
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from .models import Product, Category
from .pagination import SimplePagination
from .serializers import ProductSerializer, CategorySerializer


class ProductFilter(FilterSet):
    name = CharFilter(field_name='title', lookup_expr='icontains')
    price_from = NumberFilter(field_name='price', lookup_expr='gte')
    price_to = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = []


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filter_class = ProductFilter
    search_fields = ['name']
    ordering_fields = ['name', 'price']
    pagination_class = SimplePagination

    def get_permissions(self):
        if self.action == 'list':
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action == 'list':
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]

    def get_serializer_context(self):
        return {'request': self.request}
