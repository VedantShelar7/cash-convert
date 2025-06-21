# converter.py

def convert_currency(amount, from_currency, to_currency):
    rates = {
        'USD': 1.0,        # base
        'INR': 83.2,
        'EUR': 0.93,
        'JPY': 157.5,
        'GBP': 0.79
    }

    if from_currency not in rates or to_currency not in rates:
        return "Unsupported currency."

    usd_amount = amount / rates[from_currency]
    converted = usd_amount * rates[to_currency]
    return round(converted, 2)

def main():
    print("💱 Currency Converter")
    amount = float(input("Enter amount: "))
    from_currency = input("From currency (e.g. USD, INR): ").upper()
    to_currency = input("To currency (e.g. EUR, JPY): ").upper()

    result = convert_currency(amount, from_currency, to_currency)
    print(f"Converted amount: {result} {to_currency}")

if __name__ == "__main__":
    main()