from rest_framework import viewsets

from modules.core.models.definitions import Marketable, Partner
from modules.core.web.serializers import MarketableSerializer, PartnerSerializer


class MarketableViewSet(viewsets.ModelViewSet):
    queryset = Marketable.objects.all().order_by("name")
    serializer_class = MarketableSerializer


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all().order_by("name")
    serializer_class = PartnerSerializer
