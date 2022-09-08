from django.shortcuts import render
from rest_framework import viewsets
from .models import Region, Location, Contact, Hotel, Food, Transport
from .serializers import RegionSerializer, ContactSerializer

class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer