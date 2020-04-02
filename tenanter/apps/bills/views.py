from django.shortcuts import render
from rest_framework import generics
from .serializers import BillsAgreementSerializer
from .models import Bills_agreement


class BillsByFlatAPIView(generics.ListAPIView):
    serializer_class = BillsAgreementSerializer

    def get_queryset(self):
        flat = self.kwargs['flat']
        return Bills_agreement.objects.filter(flat=flat)


class BillsEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bills_agreement.objects.all()
    serializer_class = BillsAgreementSerializer


class FlatBillsCreationAPIView(generics.ListCreateAPIView):  # TODO: only create
    queryset = Bills_agreement.objects.all()
    serializer_class = BillsAgreementSerializer
