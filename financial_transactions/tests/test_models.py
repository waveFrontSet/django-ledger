import pytest

from financial_transactions.models import Party, Transaction

pytestmark = pytest.mark.django_db


def test_party_str(party: Party) -> None:
    assert party.name in str(party)


class TestTransactionStr:
    def test_date_in_str(self, transaction: Transaction) -> None:
        assert transaction.valid_at in str(transaction)

    def test_sender_in_str(self, transaction: Transaction) -> None:
        assert str(transaction.sender) in str(transaction)

    def test_recipient_in_str(self, transaction: Transaction) -> None:
        assert str(transaction.recipient) in str(transaction)

    def test_amount_in_str(self, transaction: Transaction) -> None:
        assert f"{transaction.amount / 100:.2f}" in str(transaction)
