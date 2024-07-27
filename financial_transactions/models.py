from django.db import models


class Party(models.Model):
    """Party of a financial transaction."""

    name = models.CharField(primary_key=True, max_length=100)

    def __str__(self) -> str:
        return self.name
