# test_generators.py

import pytest
from generators import filter_by_currency, transaction_descriptions, card_number_generator


# Тестирование filter_by_currency
def test_filter_by_currency():
    transactions = [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}},
        {"id": 2, "operationAmount": {"currency": {"code": "EUR"}}}
    ]

    usd_transactions = filter_by_currency(transactions, "USD")
    result = list(usd_transactions)
    assert len(result) == 1
    assert result[0]['id'] == 1

    eur_transactions = filter_by_currency(transactions, "EUR")
    result = list(eur_transactions)
    assert len(result) == 1
    assert result[0]['id'] == 2

    # Пустой список
    empty_transactions = []
    empty_result = list(filter_by_currency(empty_transactions, "USD"))
    assert empty_result == []


# Тестирование transaction_descriptions
def test_transaction_descriptions():
    transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"}
    ]

    descriptions = transaction_descriptions(transactions)
    result = list(descriptions)
    assert result == ["Перевод организации", "Перевод со счета на счет"]

    # Пустой список
    empty_transactions = []
    empty_result = list(transaction_descriptions(empty_transactions))
    assert empty_result == []


# Тестирование card_number_generator
def test_card_number_generator():
    card_generator = card_number_generator(1, 5)
    result = list(card_generator)
    assert len(result) == 5
    assert result[0] == '0000 0000 0000 0001'
    assert result[-1] == '0000 0000 0000 0005'

    # Тест с крайними значениями
    card_generator = card_number_generator(9999999999999995, 9999999999999999)
    result = list(card_generator)
    assert len(result) == 5
    assert result[0] == '9999 9999 9999 9995'
    assert result[-1] == '9999 9999 9999 9999'

    # Тест с пустым диапазоном
    card_generator = card_number_generator(1, 0)
    result = list(card_generator)
    assert result == []
