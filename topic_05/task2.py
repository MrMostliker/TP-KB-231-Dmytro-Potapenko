import urllib.request
import json


def get_exchange_rate(currency_code):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code}&json"
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            rates = json.loads(data)
            if rates:
                return rates[0]["rate"]  
            else:
                print(f"Currency {currency_code} not found in NBU data.")
                return None
    except Exception as e:
        print(f"Error fetching exchange rate: {e}")
        return None


def currency_converter():
    supported_currencies = {"EUR": "Євро", "USD": "Долар США", "PLN": "Польський злотий"}
    print("Supported currencies: EUR, USD, PLN")
    currency = input("Enter the currency code (EUR, USD, PLN): ").strip().upper()

    if currency not in supported_currencies:
        print("Unsupported currency. Please choose from EUR, USD, PLN.")
        return

    try:
        amount = float(input(f"Enter the amount in {currency}: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    rate = get_exchange_rate(currency)
    if rate:
        converted_amount = round(amount * rate, 2)
        print(f"{amount} {currency} = {converted_amount} UAH")
    else:
        print("Conversion failed due to issues with fetching the exchange rate.")


if __name__ == "__main__":
    currency_converter()
