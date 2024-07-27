from django.db import models


class Party(models.Model):
    """Party of a financial transaction."""

    name = models.CharField(primary_key=True, max_length=100)

    def __str__(self) -> str:
        return self.name


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
