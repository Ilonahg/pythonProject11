# generators.py

from typing import List, Dict, Iterator

def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Генератор, который фильтрует транзакции по валюте.
    :param transactions: Список транзакций.
    :param currency: Валюта для фильтрации.
    :return: Итератор транзакций с заданной валютой.
    """
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency:
            yield transaction

def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор, который возвращает описание каждой транзакции.
    :param transactions: Список транзакций.
    :return: Итератор строк с описаниями транзакций.
    """
    for transaction in transactions:
        yield transaction['description']

def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.
    :param start: Начальное значение диапазона.
    :param end: Конечное значение диапазона.
    :return: Итератор с номерами карт.
    """
    for num in range(start, end + 1):
        yield f'{num:016d}'[:4] + ' ' + f'{num:016d}'[4:8] + ' ' + f'{num:016d}'[8:12] + ' ' + f'{num:016d}'[12:]
