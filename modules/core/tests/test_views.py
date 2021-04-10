import logging
from uuid import UUID

import pytest
from rest_framework import status

from modules.core.models.definitions import MarketableKind


@pytest.mark.django_db
class TestMarketableViewSet:
    def test_must_create_with_a_post(self, api):

        result = api.post(
            "/api/core/marketables/",
            data={"name": "New Service", "kind": "Service"},
            format="json",
        )
        assert result
        assert result.status_code == status.HTTP_201_CREATED, result.status_text
        assert UUID(result.data["id"])