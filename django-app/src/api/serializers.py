from rest_framework import serializers
from .models import Business, Happyhour


class BusinessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business
        fields = '__all__'


class HappyhourSerializer(serializers.ModelSerializer):

    class Meta:
        model = Happyhour
        fields = '__all__'