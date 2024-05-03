from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    exchange_rate = c.get_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate
    return converted_amount

amount = float(input("Enter the amount: "))
from_currency = input("Convert from currency: ").upper()
to_currency = input("Convert to currency: ").upper()

result = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {result} {to_currency}")
