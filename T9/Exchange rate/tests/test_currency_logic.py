import os
import pytest
from app.currency_logic import load_exchange_rates, update_exchange_rates, convert_currency

def test_load_exchange_rates():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'exchange_rates.json')
    exchange_rates = load_exchange_rates(file_path)
    assert 'base' in exchange_rates
    assert 'rates' in exchange_rates
    assert isinstance(exchange_rates['rates'], dict)

def test_update_exchange_rates():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'exchange_rates.json')
    new_rates = {"base": "USD", "rates": {"EUR": 0.85, "GBP": 0.76, "JPY": 110.12, "AUD": 1.35}}
    update_exchange_rates(file_path, new_rates)
    updated_rates = load_exchange_rates(file_path)
    assert new_rates == updated_rates

def test_convert_currency():
    exchange_rates = {"base": "USD", "rates": {"EUR": 0.85, "GBP": 0.76, "JPY": 110.12, "AUD": 1.35}}
    amount = 100
    from_currency = "EUR"
    to_currency = "JPY"
    converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
    assert converted_amount == pytest.approx(12955.76, 0.01)
