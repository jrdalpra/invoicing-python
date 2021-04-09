from rest_framework import routers

from modules.core.web import views

router = routers.DefaultRouter()
router.register(r"marketables", views.MarketableViewSet)


