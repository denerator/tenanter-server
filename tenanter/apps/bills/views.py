import datetime
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from tenanter.apps.flat.models import Flat
from . import serializers
from .models import BillsAgreement, BillsHistory


class BillsByFlatAPIView(generics.ListAPIView):
    """Get bills agreement by flat"""
    serializer_class = serializers.BillsAgreementSerializer

    def get_queryset(self):
        flat = self.kwargs['flat']
        return BillsAgreement.objects.filter(flat=flat)


class BillEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Edit bill agreement by pk"""
    queryset = BillsAgreement.objects.all()
    serializer_class = serializers.BillsAgreementSerializer


class FlatBillsCreationAPIView(generics.ListCreateAPIView):
    """Create bill agreement"""
    queryset = BillsAgreement.objects.all()
    serializer_class = serializers.BillsAgreementSerializer


class BillsHistoryCreationAPIView(generics.CreateAPIView):
    """Insert bill value by month"""
    serializer_class = serializers.BillsHistoryCreationSerializer
    queryset = BillsHistory.objects.all()

    def create(self, request):
        """
            Check if bill record with current month does not exists
            If bill is dynamic calculate difference from previous month value
        """
        today = datetime.date.today()

        flat = Flat.objects.get(pk=request.data['flat'])
        value = request.data['value']

        try:
            bill = BillsAgreement.objects.get(pk=request.data['bill'])
        except ObjectDoesNotExist:
            raise ValidationError('Bill does not exist')

        if BillsHistory.objects.filter(bill=bill, flat=flat, date__month=today.month).exists():
            raise ValidationError('You passed bill value this month already')

        if bill.is_dynamic:
            try:
                previous_month = BillsHistory.objects.get(
                    bill=bill, flat=flat, date__month=today.month - 1)
                difference = request.data['value'] - previous_month.value
                total = difference * bill.rate

            except ObjectDoesNotExist:
                difference = total = 0
        else:
            total = bill.rate
            value = difference = None

        bill_record = BillsHistory(flat=flat, date=today, bill=bill,
                                   rate=bill.rate, value=value, difference=difference, total=total)
        bill_record.save()
        serializer = serializers.BillsHistorySerializer(bill_record)

        return Response(serializer.data, status.HTTP_201_CREATED)


class BillsHistoryByFlatAPIView(generics.ListAPIView):
    """Get bills history by flat"""
    serializer_class = serializers.BillsHistorySerializer

    def get_queryset(self):
        flat = self.kwargs['flat']
        return BillsHistory.objects.filter(flat=flat)

# TODO: merge these endpoints to one with optional parameters


class BillHistoryAPIView(generics.ListAPIView):
    """Get bill history by flat and bill"""
    serializer_class = serializers.BillsHistorySerializer

    def get_queryset(self):
        flat = self.request.query_params.get('flat')
        bill = self.request.query_params.get('bill')
        return BillsHistory.objects.filter(flat=flat, bill=bill)
