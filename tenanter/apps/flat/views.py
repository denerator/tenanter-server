from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializers import FlatSerializer, TenantSerializer, FlatWithTenantSerializer, BillsAgreementSerializer
from .models import Flat, Tenant


class FlatCreationApiView(generics.CreateAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class FlatDetailsApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatWithTenantSerializer


class FlatsByUser(APIView):
    def get(self, request, user_id):
        # For MVP only owner can access flats
        flats = Flat.objects.filter(owner=user_id)
        serializer = FlatSerializer(flats, many=True)
        return Response(serializer.data)


class TenantSigningAPIView(generics.ListCreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class TenantEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
