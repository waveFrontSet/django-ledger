import factory
from financial_transactions.models import Party, Transaction


class PartyFactory(factory.django.DjangoModelFactory):
    """Factory producing parties (for financial transactions, not the fun ones)."""

    class Meta:
        model = Party

    name = factory.Faker("name")


class TransactionFactory(factory.django.DjangoModelFactory):
    """Factory producing financial transactions from one party to another."""

    class Meta:
        model = Transaction

    valid_at = factory.Faker("date")
    sender = factory.SubFactory(PartyFactory)
    recipient = factory.SubFactory(PartyFactory)
    amount = factory.Faker("pyint", min_value=1)
