from rest_framework import serializers
from .models import Flat, Tenant, Bills_agreement


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


class BillsAgreementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bills_agreement
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['id', 'flat', 'name', 'rate', 'is_dynamic']


class FlatWithTenantSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer()
    bills_agreement = BillsAgreementSerializer(many=True)

    class Meta:
        model = Flat
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['id', 'address', 'owner', 'tenant', 'bills_agreement']
