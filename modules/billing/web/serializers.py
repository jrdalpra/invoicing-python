import logging

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from modules.billing.models.definitions import Invoice, InvoiceItem
from modules.core.models.definitions import Marketable
from modules.core.web.serializers import MarketableSerializer, PartnerSimpleSerializer


class InvoiceItemSerializer(serializers.HyperlinkedModelSerializer):

    content = MarketableSerializer()

    class Meta:
        model = InvoiceItem
        fields = [
            "url",
            "id",
            "content",
            "quantity",
            "price",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    seller = PartnerSimpleSerializer()
    buyer = PartnerSimpleSerializer()
    items = InvoiceItemSerializer(many=True, allow_null=True, required=False)

    def create(self, validated_data):
        items = validated_data.pop("items", [])
        root = Invoice.objects.create(**validated_data)
        for item in items:
            InvoiceItem.objects.create(invoice=root, **item)
        return root

    def update(self, instance, validated_data):
        logging.error(f"{validated_data} {self.data=}")
        items = validated_data.pop("items", [])
        updated = super(InvoiceSerializer, self).update(instance, validated_data)

        raw_data = self.context["request"].data
        for i, item in enumerate(items):
            if "id" in item:
                self.fields["items"].update(
                    InvoiceItem.objects.get(id=item["id"]), item
                )
            else:
                new = raw_data["items"][i]
                content = get_object_or_404(Marketable, pk=new["content"]["id"])
                new["content"] = content
                InvoiceItem.objects.create(invoice=updated, **new)

        updated.refresh_from_db()
        return updated

    class Meta:
        model = Invoice
        fields = [
            "url",
            "id",
            "seller",
            "buyer",
            "due_at",
            "items",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
