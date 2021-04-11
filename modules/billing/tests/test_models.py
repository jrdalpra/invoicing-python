from decimal import Decimal

import pytest
from django.utils import timezone

from modules.billing.models.definitions import Invoice, InvoiceItem
from modules.core.models.definitions import Partner, Marketable, MarketableKind


@pytest.mark.django_db
class TestInvoice:
    def test_when_created_an_invoice_total_must_be_expected(self):
        expected_total = Decimal("1.000000000000")

        seller = Partner.objects.create(name="Seller")
        buyer = Partner.objects.create(name="Buyer")
        service = Marketable.objects.create(name="Service", kind=MarketableKind.SERVICE)

        subject = Invoice(seller=seller, buyer=buyer, due_at=timezone.now())
        subject.items.add(
            InvoiceItem(content=service, quantity=0.01, price=100), bulk=False
        )
        subject.save()

        assert subject.total == expected_total
