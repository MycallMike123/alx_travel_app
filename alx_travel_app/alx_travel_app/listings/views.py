from django.shortcuts import render
from rest_framework import viewsets
from .models import TravelListing
from .serializers import TravelListingSerializer

# Create your views here.
class TravelListingViewSet(viewsets.ModelViewSet):
    queryset = TravelListing.objects.all()
    serializer_class = TravelListingSerializer