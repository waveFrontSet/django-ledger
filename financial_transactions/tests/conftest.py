import pytest

from financial_transactions.models import Party, Transaction

from .factories import PartyFactory, TransactionFactory


@pytest.fixture
def party() -> Party:
    return PartyFactory()


@pytest.fixture
def transaction() -> Transaction:
    return TransactionFactory()
