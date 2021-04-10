from django.db import models
from django.utils.translation import gettext_lazy as _
from enum import Enum, unique

from modules.core.models.abstractions import BaseModel


@unique
class MarketableKind(str, Enum):
    PRODUCT = "PRODUCT"
    SERVICE = "SERVICE"

    @classmethod
    def choices(cls):
        return tuple((i.value, _(i.name.capitalize())) for i in cls)


class Marketable(BaseModel):
    name = models.CharField(max_length=1024, verbose_name="Name")
    kind = models.CharField(
        max_length=1024,
        choices=MarketableKind.choices(),
        null=False,
        blank=True,
        default=MarketableKind.PRODUCT.value,
        verbose_name=_("Kind"),
    )

    def __str__(self):
        return f"{self.name} (kind={self.kind}, id={self.id})"


class Partner(BaseModel):

    name = models.CharField(max_length=1024, verbose_name="Name")

    def __str__(self):
        return f"{self.name} (id={self.id})"
