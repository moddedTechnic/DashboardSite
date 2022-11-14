from __future__ import annotations

from typing import Iterable

from django.db import models
from pipe import where, select


class AmortisationTarget(models.Model):
    tag = models.CharField(max_length=32)
    name = models.CharField(max_length=32, null=True)
    target = models.IntegerField()

    def __str__(self) -> str:
        return self.name if self.name else self.tag

    @classmethod
    def all(cls) -> Iterable[AmortisationTarget]:
        yield from cls.objects.all()


class Transaction(models.Model):
    """Represents a transaction"""

    DIRECTIONS = (
        ('I', 'In'),
        ('O', 'Out'),
    )
    METHODS = (
        ('A', 'Amortisation'),
        ('B', 'Bacs'),
        ('C', 'Card'),
        ('S', 'Cash'),
        ('Q', 'Cheque'),
        ('P', 'PayPal'),
    )
    CATEGORIES = (
        ('A', 'Allowance'),
        ('F', 'Food'),
        ('L', 'Leisure'),
        ('O', 'Offer'),
        ('T', 'Transport'),
        ('_', 'Other'),
    )

    direction = models.CharField(max_length=1, choices=DIRECTIONS)
    amount = models.IntegerField()
    method = models.CharField(max_length=1, choices=METHODS)
    category = models.CharField(max_length=1, choices=CATEGORIES)
    date = models.DateField()
    participant = models.CharField(max_length=64, null=True, blank=True)
    amortisation = models.ForeignKey(AmortisationTarget, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        direction = 'from' if self.direction == 'I' else 'to'
        return f'£{self.get_amount()} {direction} {self.participant} ({self.date})'

    def get_amount(self) -> str:
        pence = str(self.amount % 100).ljust(2, '0')
        return f'{self.amount // 100}.{pence}'

    def get_value(self) -> int:
        return self.amount * (1 if self.direction == 'I' else -1)

    def get_amortisation_name(self) -> str:
        if self.amortisation is None:
            return ''
        return str(self.amortisation)

    @classmethod
    def all(cls) -> Iterable[Transaction]:
        yield from cls.objects.all()

    @classmethod
    def dates(cls) -> Iterable[datetime]:
        return Transaction.all() | where(lambda t: True if t.amortisation is None else (t.method == 'A')) \
                                 | select(lambda t: t.date)

    class Meta:
        ordering = ['-date']
