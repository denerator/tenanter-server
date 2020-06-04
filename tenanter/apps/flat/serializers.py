import datetime
from rest_framework import serializers
from tenanter.apps.bills.serializers import BillsAgreementSerializer, BillsHistorySerializer, PaymentHistorySerializer
from .models import Flat, Tenant


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ['id', 'signing_date', 'payment_day',
                  'contract_time', 'rental_rate', 'deposit', 'name', 'phone', 'flat']


class FlatSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer(read_only=True)

    days_before_payment = serializers.SerializerMethodField(
        'get_days_before_payment')

    class Meta:
        model = Flat
        fields = ['id', 'address', 'owner', 'days_before_payment', 'tenant']

    def get_days_before_payment(self, obj):
        days_before_payment = 0
        if not hasattr(obj, 'tenant'):
            return days_before_payment

        today = datetime.date.today()
        month = today.month

        if obj.tenant.payment_day < today.day:
            month += 1

        payment_date = f'{today.year}-{month}-{obj.tenant.payment_day}'
        return self.days_between_today(payment_date, today)

    def days_between_today(self, date, today):
        d1 = datetime.datetime.strptime(today.isoformat(), "%Y-%m-%d")
        d2 = datetime.datetime.strptime(date, "%Y-%m-%d")
        return abs((d2 - d1).days)


class FlatWithTenantSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer(read_only=True)
    bills_agreement = BillsAgreementSerializer(many=True, read_only=True)
    bills_history = BillsHistorySerializer(many=True, read_only=True)
    payment_history = PaymentHistorySerializer(many=True, read_only=True)
    to_pay = serializers.SerializerMethodField('get_pay_amount')

    class Meta:
        model = Flat
        fields = ['id', 'address', 'owner', 'tenant',
                  'bills_agreement', 'bills_history', 'payment_history', 'to_pay']

    def get_pay_amount(self, obj):
        """Return how much you should pay for the flat in this month"""
        today = datetime.date.today()

        month_bills = BillsHistorySerializer(obj.bills_history.filter(
            flat=obj.id, date__month=today.month, date__year=today.year), many=True)

        total = 0

        for bill in month_bills.data:
            total += bill['total']

        if hasattr(obj, 'tenant'):
            total += obj.tenant.rental_rate

        return total
