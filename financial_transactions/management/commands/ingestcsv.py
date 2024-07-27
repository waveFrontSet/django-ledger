import argparse
import csv
from typing import Any

from django.core.management.base import BaseCommand

from financial_transactions.models import Party, Transaction


class Command(BaseCommand):
    help = "Ingest a csv file of transactions"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=argparse.FileType(mode="r"))

    def handle(self, *args: Any, **options: Any) -> None:
        csv_file = options["csv_file"]
        with csv_file as f:
            reader = csv.DictReader(
                f, fieldnames=("valid_at", "sender", "recipient", "amount")
            )
            for row in reader:
                sender = Party.objects.get_or_create(name=row["sender"])[0]
                recipient = Party.objects.get_or_create(name=row["recipient"])[0]
                Transaction.objects.create(
                    valid_at=row["valid_at"],
                    sender=sender,
                    recipient=recipient,
                    amount=int(float(row["amount"]) * 100),
                )
