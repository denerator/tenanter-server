from rest_framework import serializers
from .models import Flat, Tenant
from tenanter.apps.bills.serializers import BillsAgreementSerializer


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ['id', 'signing_date', 'payment_day',
                  'contract_time', 'rental_rate', 'deposit', 'name', 'phone', 'flat']


class FlatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flat
        fields = ['id', 'address', 'owner']


class FlatWithTenantSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer(read_only=True)
    bills_agreement = BillsAgreementSerializer(many=True, read_only=True)

    class Meta:
        model = Flat
        fields = ['id', 'address', 'owner', 'tenant', 'bills_agreement']
