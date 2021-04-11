from rest_framework import routers

from modules.billing.web import views

router = routers.DefaultRouter()
router.register(r"invoices", views.InvoiceViewSet)
router.register(r"invoiceitems", views.InvoiceItemViewSet)
