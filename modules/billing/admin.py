from django.contrib import admin

# Register your models here.
from modules.billing.models.definitions import Invoice

admin.site.register(Invoice)
