from rest_framework import serializers
from .models import BillsAgreement, BillsHistory, PaymentHistory


class BillsAgreementSerializer(serializers.ModelSerializer):
    """Bills agreement serializer"""
    class Meta:
        model = BillsAgreement
        fields = ['id', 'flat', 'name', 'rate', 'is_dynamic']


class BillsHistoryCreationSerializer(serializers.ModelSerializer):
    """Bills history creation serializer"""
    class Meta:
        model = BillsHistory
        fields = ['flat', 'bill', 'value']


class BillsHistorySerializer(serializers.ModelSerializer):
    """Bills history retriving serializer"""
    bill = serializers.StringRelatedField()

    class Meta:
        model = BillsHistory
        fields = ['id', 'flat', 'date', 'bill',
                  'value', 'rate', 'difference', 'total']


class PaymentHistoryCreationSerializer(serializers.ModelSerializer):
    """Payment history creation serializer"""

    class Meta:
        model = PaymentHistory
        fields = ['flat', 'date', 'tenant']


class PaymentHistorySerializer(serializers.ModelSerializer):
    """Payment history retriving serializer"""
    tenant = serializers.StringRelatedField()

    class Meta:
        model = PaymentHistory
        fields = ['id', 'flat', 'date', 'bills', 'tenant',
                  'rental_rate', 'total']
