import json

def load_exchange_rates(file_path):
    with open(file_path, 'r') as file:
        exchange_rates = json.load(file)
    return exchange_rates

def update_exchange_rates(file_path, new_rates):
    with open(file_path, 'w') as file:
        json.dump(new_rates, file)

def convert_currency(amount, from_currency, to_currency, exchange_rates):
    base_currency = exchange_rates['base']
    rates = exchange_rates['rates']

    if from_currency != base_currency:
        amount = amount / rates[from_currency]

    return amount * rates[to_currency]
