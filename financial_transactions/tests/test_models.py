import pytest

from financial_transactions.models import Party

pytestmark = pytest.mark.django_db


def test_party_str(party: Party) -> None:
    assert party.name in str(party)
