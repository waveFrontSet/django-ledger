import pytest

from .factories import PartyFactory, TransactionFactory
from financial_transactions.models import Party, Transaction


@pytest.fixture
def party() -> Party:
    return PartyFactory()


@pytest.fixture
def transaction() -> Transaction:
    return TransactionFactory()
