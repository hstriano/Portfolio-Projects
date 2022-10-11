# Currency Converter

import requests

class Currency_converter:
    # empty dictionary to store conversion rates
    rates = {}
    def __init__(self, url):
        data = requests.get(url).json()

        # Extract rates from json
        self.rates = data["rates"]

    # cross multiplication between rates
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]

        # set to 2 decimal places
        amount = round(amount * self.rates[to_currency], 2)
        print("{} {} = {} {}".format(initial_amount, from_currency, to_currency))

# main program
if __name__ == "__main__":

    YOUR_ACCESS_KEY = 'QEZp3BI7CpxaTaU6Mia6NNsKXDb8zjZi'
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', YOUR_ACCESS_KEY)
    c = Currency_converter(url)
    from_country = input("From Country: ")
    to_country = input("To Country: ")
    amount = int(input("Amount: "))

    c.convert(from_country, to_country, amount)