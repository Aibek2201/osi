from rest_framework.viewsets import ModelViewSet

from . import serializers, models


class HouseViewSet(ModelViewSet):
    serializer_class = serializers.HouseSerializer
    queryset = models.House.objects.all()

