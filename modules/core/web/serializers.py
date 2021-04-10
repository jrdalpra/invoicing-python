from rest_framework import serializers

from modules.core.models.definitions import Marketable, Partner


class MarketableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marketable
        fields = ["id", "name", "kind", "created_at", "updated_at", "url"]
        read_only_fields = ["id", "created_at", "updated_at"]


class PartnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partner
        fields = ["id", "name", "kind", "created_at", "updated_at", "url"]
        read_only_fields = ["id", "created_at", "updated_at"]
