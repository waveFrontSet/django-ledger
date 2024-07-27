from datetime import date

import pytest

from financial_transactions.models import Party, Transaction

from .factories import PartyFactory, TransactionFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def john() -> Party:
    return PartyFactory(name="john")


@pytest.fixture
def mary() -> Party:
    return PartyFactory(name="mary")


@pytest.fixture
def supermarket() -> Party:
    return PartyFactory(name="supermarket")


@pytest.fixture(autouse=True)
def required_transactions(
    john: Party, mary: Party, supermarket: Party
) -> list[Transaction]:
    return [
        TransactionFactory(
            valid_at="2015-01-16",
            sender=john,
            recipient=mary,
            amount=12500,
        ),
        TransactionFactory(
            valid_at="2015-01-17",
            sender=john,
            recipient=supermarket,
            amount=2000,
        ),
        TransactionFactory(
            valid_at="2015-01-17",
            sender=mary,
            recipient__name="insurance",
            amount=10000,
        ),
    ]


def test_john_has_correct_balance(john: Party) -> None:
    assert john.balance() == -14500


def test_supermarket_has_correct_balance(supermarket: Party) -> None:
    assert supermarket.balance() == 2000


@pytest.mark.parametrize(
    ["valid_at", "balance"],
    [
        pytest.param(date(2015, 1, 16), 0, id="balance_before_transactions"),
        pytest.param(date(2015, 1, 17), 12500, id="balance_after_transactions"),
    ],
)
def test_mary_has_correct_balance(mary: Party, valid_at: date, balance: int) -> None:
    assert mary.balance(valid_at) == balance
