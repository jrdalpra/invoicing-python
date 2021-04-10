import logging
from uuid import UUID

import pytest
from rest_framework import status

from modules.core.models.definitions import MarketableKind, Marketable


@pytest.mark.django_db
class TestMarketableViewSet:
    def test_create(self, api):

        result = api.post(
            "/api/core/marketables/",
            data={"name": "New Service", "kind": MarketableKind.SERVICE},
            format="json",
        )
        logging.info(f"{result=} {result.status_text=} {result.data=}")

        assert result
        assert result.status_code == status.HTTP_201_CREATED, result.status_text
        assert UUID(result.data["id"])

    @pytest.fixture()
    def existing_marketable(self):
        existing = Marketable.objects.create(
            name="Existing Service", kind=MarketableKind.SERVICE
        )
        return {"object": existing, "endpoint": f"/api/core/marketables/{existing.id}/"}

    def test_get(self, api, existing_marketable):

        result = api.get(existing_marketable["endpoint"])
        logging.info(f"{result=} {result.status_text=} {result.data=}")

        assert result
        assert result.status_code == status.HTTP_200_OK
        assert result.data["name"] == "Existing Service"
        assert result.data["kind"] == MarketableKind.SERVICE.value

    def test_update(self, api, existing_marketable):
        endpoint = existing_marketable["endpoint"]
        expected_new_name = "New Name For Existing Service"

        result = api.put(endpoint, data={"name": expected_new_name})
        assert result
        assert result.status_code == status.HTTP_200_OK

        result = api.get(endpoint)
        logging.info(f"{result=} {result.status_text=} {result.data=}")

        assert result
        assert result.status_code == status.HTTP_200_OK
        assert result.data["name"] == expected_new_name
        assert result.data["kind"] == MarketableKind.SERVICE.value

    def test_delete_soft(self, api, existing_marketable):
        endpoint = existing_marketable["endpoint"]

        result = api.delete(endpoint)
        assert result
        assert result.status_code == status.HTTP_204_NO_CONTENT

        result = api.get(endpoint)
        logging.info(f"{result=} {result.status_text=} {result.data=}")

        assert result
        assert result.status_code == status.HTTP_404_NOT_FOUND
