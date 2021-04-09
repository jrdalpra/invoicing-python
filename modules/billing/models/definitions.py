from decimal import Decimal

from django.db import models

from modules.core.models.abstractions import BaseModel
from modules.core.models.definitions import Partner, Marketable


class Invoice(BaseModel):

    seller = models.ForeignKey(Partner, related_name="+", on_delete=models.CASCADE)
    buyer = models.ForeignKey(Partner, related_name="+", on_delete=models.CASCADE)
    due_at = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        total = Decimal('0')
        for item in self.items.all():
            total += item.total
        return total


class InvoiceItem(BaseModel):

    invoice = models.ForeignKey(Invoice, related_name="items", on_delete=models.CASCADE)
    content = models.ForeignKey(Marketable, related_name="+", on_delete=models.PROTECT)
    quantity = models.DecimalField(
        max_digits=12, decimal_places=6, default=0, null=False
    )
    price = models.DecimalField(max_digits=15, decimal_places=6, default=0, null=False)

    @property
    def total(self):
        return self.quantity * self.price
