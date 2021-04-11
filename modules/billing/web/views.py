from rest_framework import viewsets

from modules.billing.models.definitions import Invoice, InvoiceItem
from modules.billing.web.serializers import InvoiceSerializer, InvoiceItemSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all().order_by("-created_at")
    serializer_class = InvoiceSerializer


class InvoiceItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
