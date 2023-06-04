from datetime import datetime, timedelta, date

from rest_framework import serializers
from customers.models import Customer, Product


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email']


class ProductSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'name', 'status', 'customer']

    def validate_status(self, value):
        created_on = self.instance.created_on if self.instance else None
        if value is False:
            if created_on:
                registered_date = created_on.date()
            else:
                registered_date = date.today()
            current_date = datetime.now().date()
            delta = current_date - registered_date
            if delta < timedelta(days=60):
                raise serializers.ValidationError(
                    "Product cannot be made inactive within 2 months of "
                    "registration.")

        return value

    def create(self, validated_data):
        customer = validated_data.pop('customer')
        customer_id = customer.id
        product = Product.objects.create(customer_id=customer_id,
                                         **validated_data)
        return product

    def update(self, instance, validated_data):
        customer = validated_data.pop('customer')
        customer_id = customer.id
        instance.customer_id = customer_id
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
