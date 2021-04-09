from rest_framework import serializers

from modules.core.models.definitions import Marketable


class MarketableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marketable
        read_only_fields = ["id", "created_at", "updated_at"]
        exclude = ["deleted_at"]
