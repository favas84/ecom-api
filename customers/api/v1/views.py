from collections import OrderedDict

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from customers.models import Customer, Product
from .serializers import CustomerSerializer, ProductSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        data = OrderedDict([
            ('customer', serializer.data),
            ('message', 'Customer added successfully.')
        ])

        return Response(data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        serializer = self.get_serializer(
            self.get_object(), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        data = OrderedDict([
            ('customer', serializer.data),
            ('message', 'Customer updated successfully.')
        ])

        return Response(data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None, *args, **kwargs):
        customer = self.get_object()
        self.perform_destroy(customer)

        data = OrderedDict([
            ('message', 'Customer deleted successfully.')
        ])

        return Response(data, status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        """
        Returns all the products related to customer.
        """
        customer = self.get_object()
        products = customer.products.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        data = OrderedDict([
            ('product', serializer.data),
            ('message', 'Product added to the customer successfully.')
        ])

        return Response(data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        serializer = self.get_serializer(
            self.get_object(), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        data = OrderedDict([
            ('product', serializer.data),
            ('message', 'Product updated successfully.')
        ])

        return Response(data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None, *args, **kwargs):
        customer = self.get_object()
        self.perform_destroy(customer)

        data = OrderedDict([
            ('message', 'Product deleted successfully.')
        ])

        return Response(data, status=status.HTTP_204_NO_CONTENT)