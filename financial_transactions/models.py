from datetime import date
from django.db import models


class Party(models.Model):
    """Party of a financial transaction."""

    name = models.CharField(primary_key=True, max_length=100)

    def __str__(self) -> str:
        return self.name

    def balance(self, valid_at: date | None = None) -> int:
        """Compute the balance of this party at the given date `valid_at`.

        If no `valid_at` date is given, we'll use the current date."""
        if valid_at is None:
            valid_at = date.today()
        sum_amount = models.Sum("amount", default=0)
        sent_transactions = Transaction.objects.filter(
            sender=self, valid_at__lt=valid_at
        ).aggregate(sum_amount)
        received_transactions = Transaction.objects.filter(
            recipient=self, valid_at__lt=valid_at
        ).aggregate(sum_amount)
        return received_transactions["amount__sum"] - sent_transactions["amount__sum"]


class Transaction(models.Model):
    """A financial transaction from one `Party` to another."""

    valid_at = models.DateField(db_index=True)
    sender = models.ForeignKey(
        to=Party,
        db_index=True,
        on_delete=models.CASCADE,
        related_name="sent_transactions",
    )
    recipient = models.ForeignKey(
        to=Party,
        db_index=True,
        on_delete=models.CASCADE,
        related_name="received_transactions",
    )
    amount = models.BigIntegerField()

    def __str__(self) -> str:
        return (
            f"{self.valid_at}: {self.sender}->{self.recipient} §{self.amount / 100:.2f}"
        )
