import requests
from prettytable import PrettyTable

api = 'https://api.coinmarketcap.com/v2/ticker/'

raw_data = requests.get(api).json()

data = raw_data['data']

currency = data['52']['name']

total_supply = data['52']['total_supply']

print ("The following currency ",currency)
print("Has the following supply ", total_supply)

table = PrettyTable()

for currency in data:
    print(data[currency]['name'], data[currency]['symbol'], data[currency]['quotes']['USD']['price'])

for currency in data:
    name = data[currency]['name']
    price = data[currency]['quotes']['USD']['price']
    mktCap = data[currency]['quotes']['USD']['market_cap']
    volume24hr = data[currency]['quotes']['USD']['volume_24h']
    percentChange1hr = data[currency]['quotes']['USD']['percent_change_1h']
    percentChange24hr = data[currency]['quotes']['USD']['percent_change_24h']

    table.add_row([name, price, mktCap, volume24hr, percentChange24hr, percentChange1hr])

table.field_names = ["Coin Name", "Current Price", "Market Cap", "24hr Volume", "24hr percent change", "1hr percent change"]
table.sortby = "24hr percent change"
table.reversesort = True


print(table)
