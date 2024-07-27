import factory
from financial_transactions.models import Party


class PartyFactory(factory.django.DjangoModelFactory):
    """Factory producing parties (for financial transactions, not the fun ones)."""

    class Meta:
        model = Party

    name = factory.Faker("name")
