from enum import Enum, unique

from django.db import models
from django.utils.translation import gettext_lazy as _

from modules.core.models.abstractions import BaseModel

@unique
class MarketableKlass(str, Enum):
    PRODUCT = "PRODUCT"
    SERVICE = "SERVICE"



    @classmethod
    def choices(cls):
        return tuple((_(i.name.capitalize()), i.value) for i in cls)


class Marketable(BaseModel):
    name = models.CharField(max_length=1024, verbose_name="Name")
    klass = models.CharField(
        max_length=1024,
        choices=MarketableKlass.choices(),
        null=False,
        blank=True,
        default=MarketableKlass.PRODUCT,
        verbose_name=_("Class"),
    )

    def __str__(self):
        return f"{self.name} (id={self.id})"
