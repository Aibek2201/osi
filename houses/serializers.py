from rest_framework import serializers

from . import models


class HouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.House
        fields = '__all__'