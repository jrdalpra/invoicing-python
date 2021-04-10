from django.db import models
from django.utils.translation import gettext_lazy as _
from enum import Enum, unique

from modules.core.models.abstractions import BaseModel


@unique
class MarketableKind(str, Enum):
    """Defines the kind of a marketable item"""

    PRODUCT = "PRODUCT"
    SERVICE = "SERVICE"

    @classmethod
    def choices(cls):
        return tuple((i.value, _(i.name.capitalize())) for i in cls)


class Marketable(BaseModel):
    """Represents anything that can be sold or marketed"""

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


class PartnerKind(str, Enum):
    """Defines the kind of a partner"""

    PERSON = "PERSON"
    ORGANIZATION = "ORGANIZATION"

    @classmethod
    def choices(cls):
        return tuple((i.value, _(i.name.capitalize())) for i in cls)


class Partner(BaseModel):
    """Represents a person or entity that will be part of any business operation"""

    name = models.CharField(max_length=1024, verbose_name="Name")
    kind = models.CharField(
        max_length=1024,
        choices=PartnerKind.choices(),
        null=False,
        blank=True,
        default=PartnerKind.ORGANIZATION.value,
        verbose_name=_("Kind"),
    )

    def __str__(self):
        return f"{self.name} (kind={self.kind}, id={self.id})"
