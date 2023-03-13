from django.contrib import admin

# Register your models here.
from modules.billing.models.definitions import Invoice, InvoiceItem


class InvoiceItemForm(admin.TabularInline):
    model = InvoiceItem
    fk_name = "invoice"


class InvoiceAdmin(admin.ModelAdmin):
    inlines = [
        InvoiceItemForm
    ]

    list_display = [
        "id",
        "seller_name",
        "buyer_name",
        "total"
    ]

    def seller_name(self, obj: Invoice):
        return str(obj.seller.name)

    def buyer_name(self, obj: Invoice):
        return str(obj.buyer.name)

    def total(self, obj: Invoice):
        return str(obj.total)


admin.site.register(Invoice, InvoiceAdmin)
