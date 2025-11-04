from rest_framework import serializers
from .models import Visitor, Visit, Office


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = '__all__'


class VisitSerializer(serializers.ModelSerializer):
    visitor = VisitorSerializer(read_only=True)
    office = OfficeSerializer(read_only=True)


    class Meta:
        model = Visit
        fields = '__all__'