import requests
from prettytable import PrettyTable

api = "https://api.binance.com/api/v1/ticker/24hr"

data = requests.get(api).json()

table = PrettyTable()

for currency in data:
    if 'BTC' in currency['symbol']:
        name = currency['symbol']
        price = currency['lastPrice']
        volume = currency['volume']
        table.add_row([name, price, volume])

table.field_names = ["Symbol", "Last Price", "Volume"]
table.sortby = "Last Price"
table.reversesort = True
print(table)
