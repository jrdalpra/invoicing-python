from rest_framework import viewsets

from modules.core.models.definitions import Marketable
from modules.core.web.serializers import MarketableSerializer


class MarketableViewSet(viewsets.ModelViewSet):
    queryset = Marketable.objects.all().order_by("name")
    serializer_class = MarketableSerializer
