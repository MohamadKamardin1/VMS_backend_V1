from rest_framework import viewsets
from .models import Visitor, Visit, Office
from .serializers import VisitorSerializer, VisitSerializer, OfficeSerializer


class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all().order_by('-created_at')
    serializer_class = VisitorSerializer


class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all().order_by('name')
    serializer_class = OfficeSerializer


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all().select_related('visitor', 'office').order_by('-check_in_time')
    serializer_class = VisitSerializer