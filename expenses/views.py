import itertools
from collections import defaultdict
from datetime import datetime, timedelta
from math import atan
from typing import Iterable

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from pipe import where, select

from .models import AmortisationTarget, Transaction


def currency_to_string(amount: int) -> str:
    return f'{amount // 100}.' + str(amount % 100).ljust(2, '0')


def calculate_amortisation_progress() -> Iterable[dict[str, str]]:
    return AmortisationTarget.all() | select(lambda a: {
        'name': str(a), 'target': f'£{currency_to_string(a.target)}',
        'progress': '£' + currency_to_string(
            sum(Transaction.all() | where(lambda t: t.amortisation == a and t.method == 'A') | select(lambda t: t.amount))
        )
    })


def calculate_balance() -> int:
    return sum(Transaction.all() | where(lambda t: True if t.amortisation is None else (t.method == 'A'))
                                 | select(lambda t: t.get_value()))


def calculate_real_balance() -> int:
    return sum(Transaction.all() | where(lambda t: True if t.amortisation is None else (t.method != 'A'))
                                 | select(lambda t: t.get_value()))


def calculate_tracking_duration() -> int:
    transaction_dates = list(Transaction.dates())
    first_day = min(transaction_dates)
    last_day = max(transaction_dates)
    return (last_day - first_day).days


def grouper(n, iterable):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk


def change_in_balance(window: int = 1) -> Iterable[int]:
    if window == 1:
        transactions = Transaction.all() | where(lambda t: True if t.amortisation is None else (t.method == 'A'))
        daily_totals = defaultdict(int)
        for transaction in transactions:
            daily_totals[transaction.date] += transaction.get_value()
        days = set(daily_totals.keys())
        first_day, *_ = sorted(days)
        for i in range(1, calculate_tracking_duration()):
            new_date = first_day + timedelta(days=i)
            if new_date not in days:
                daily_totals[new_date] = 0
        yield from list(sorted(daily_totals.items()) | select(lambda t: t[1]))
        return
    for g in grouper(window, change_in_balance(1)):
        yield sum(g)


def balance_over_time() -> Iterable[int]:
    previous_balance = 0
    for b in change_in_balance():
        previous_balance += b
        yield previous_balance


def viability(time: int, window: int) -> float:
    return atan(list(change_in_balance(window))[time]) / 2


def viability_over_time(window: int) -> Iterable[float]:
    for i in range(calculate_tracking_duration() // window):
        yield viability(i, window)


def index(request: HttpRequest) -> HttpResponse:
    # TODO: balance viability
    return render(request, 'expenses/index.html', {
        'transactions': Transaction.all(),
        'balance': f'£{currency_to_string(calculate_balance())}',
        'real_balance': f'£{currency_to_string(calculate_real_balance())}',
        'amortisations': calculate_amortisation_progress(),
    })


def data_income(request: HttpRequest) -> HttpResponse:
    transactions = list(Transaction.objects.filter(direction='I'))
    if 'window' in request.GET:
        window_size = int(request.GET.get('window', '0'))
        threshold = (datetime.today() - timedelta(days=window_size)).date()
        transactions |= where(lambda t: t.date >= threshold)
    groups = defaultdict(int)
    for transaction in transactions:
        groups[transaction.get_category_display()] += transaction.amount
    return JsonResponse(groups)


def data_expenditure(request: HttpRequest) -> HttpResponse:
    transactions = list(Transaction.objects.filter(direction='O'))
    if 'window' in request.GET:
        window_size = int(request.GET.get('window', '0'))
        threshold = (datetime.today() - timedelta(days=window_size)).date()
        transactions |= where(lambda t: t.date >= threshold)
    groups = defaultdict(int)
    for transaction in transactions:
        groups[transaction.get_category_display()] += transaction.amount
    return JsonResponse(groups)
