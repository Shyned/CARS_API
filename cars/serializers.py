from rest_framework import serializer
from .models import Car



class CarSerializer(serializer.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id','make','model','year','price']




