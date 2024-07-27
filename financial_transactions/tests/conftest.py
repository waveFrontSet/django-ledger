import pytest

from .factories import PartyFactory
from financial_transactions.models import Party


@pytest.fixture
def party() -> Party:
    return PartyFactory()
