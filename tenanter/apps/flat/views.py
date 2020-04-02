from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializers import FlatSerializer, TenantSerializer, FlatWithTenantSerializer
from .models import Flat, Tenant


class FlatCreationApiView(generics.CreateAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class FlatDetailsApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class FlatsByUser(APIView):
    def get(self, request, user_id):
        flats = Flat.objects.filter(owner=user_id) # For MVP only owner can access flats
        serializer = FlatWithTenantSerializer(flats, many=True)
        return Response(serializer.data)


class TenantSigningAPIView(generics.ListCreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
