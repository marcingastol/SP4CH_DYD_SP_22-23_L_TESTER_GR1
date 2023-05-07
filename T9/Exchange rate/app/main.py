import os
from app.currency_logic import load_exchange_rates, update_exchange_rates, convert_currency

def main():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'exchange_rates.json')
    exchange_rates = load_exchange_rates(file_path)

    amount = 100
    from_currency = 'EUR'
    to_currency = 'JPY'

    converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
    print(f'{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}')

if __name__ == '__main__':
    main()
