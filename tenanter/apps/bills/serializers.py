from rest_framework import serializers
from .models import Bills_agreement


class BillsAgreementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bills_agreement
        fields = ['id', 'flat', 'name', 'rate', 'is_dynamic']
