import pytest

from modules.core.models.definitions import Marketable, MarketableKlass


@pytest.mark.django_db
class TestMarketable:
    @pytest.fixture()
    def subject(self):
        subject = Marketable(name="Test", klass=MarketableKlass.PRODUCT)
        subject.save()
        return subject

    def test_string_representation(self, subject: Marketable):
        assert str(subject) == f"Test (id={subject.id})"

    def test_basic_fields(self, subject: Marketable):
        assert subject.created_at is not None
        assert subject.updated_at is not None
        assert subject.deleted is False

    def test_soft_delete(self, subject: Marketable):
        subject.delete()
        assert subject.deleted is True

        subject.restore()
        assert subject.deleted is False

    def test_soft_delete_using_queryset(self, subject: Marketable):
        assert Marketable.objects.count() == 1
        Marketable.objects.all().delete()
        assert Marketable.objects.count() == 0

    def test_raw_query_set(self, subject: Marketable):
        assert Marketable.objects.get_raw_queryset().count() == 1

    def test_force_delete(self, subject: Marketable):
        assert Marketable.objects.get_raw_queryset().count() == 1
        subject.force_delete()
        assert Marketable.objects.get_raw_queryset().count() == 0
