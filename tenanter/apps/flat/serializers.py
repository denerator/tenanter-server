from rest_framework import serializers
from .models import Flat, Tenant


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['id', 'signing_date', 'payment_day',
                  'contract_time', 'rental_rate', 'deposit', 'name', 'phone', 'flat']


class FlatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flat
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['id', 'address', 'owner']


class FlatWithTenantSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer()
    class Meta:
        model = Flat
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['id', 'address', 'owner', 'tenant']
