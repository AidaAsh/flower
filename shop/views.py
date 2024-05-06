import django_filters
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action

from .serializers import *
from django_filters import rest_framework as filters
from rest_framework import filters as search
from django_filters import FilterSet, RangeFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from shop.models import *


class ProductFilter(FilterSet):
    price = RangeFilter()
    label = django_filters.ModelChoiceFilter(field_name='label', queryset=Label.objects.all())
    category = django_filters.ModelChoiceFilter(field_name='category', queryset=Category.objects.all())
    flower = django_filters.ModelChoiceFilter(field_name='composition_product__id_flower', queryset=Flower.objects.all())

    class Meta:
        model = Product
        fields = ['price', 'label', 'category', 'flower']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.DjangoFilterBackend, search.SearchFilter, search.OrderingFilter]
    search_fields = ['title', 'category__title', 'description', 'label__title']
    filterset_fields = ['category', 'label', 'composition_product__id_flower']
    ordering_fields = ['price']
    filterset_class = ProductFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.DjangoFilterBackend, search.SearchFilter, search.OrderingFilter]
    search_fields = ['title']


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [filters.DjangoFilterBackend, search.SearchFilter, search.OrderingFilter]
    filterset_fields = ['id_product__title']
    ordering_fields = ['rating']


class FlowerViewSet(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer


class CompositionViewSet(viewsets.ModelViewSet):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressSerializer
