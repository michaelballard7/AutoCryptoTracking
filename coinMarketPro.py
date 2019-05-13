import requests
from prettytable import PrettyTable

from keys import KEY


#region
key = KEY
#endregion

api = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY='


api += key

raw_data = requests.get(api).json()

data = raw_data['data']



table = PrettyTable()

for currency in data:
    name = currency['name']
    price = currency['quote']['USD']['price']
    mktCap = currency ['quote']['USD']['market_cap']
    volume24hr = currency['quote']['USD']['volume_24h']
    percentChange1hr = currency['quote']['USD']['percent_change_1h']
    percentChange24hr = currency['quote']['USD']['percent_change_24h']


    table.add_row([name, price, mktCap, volume24hr, percentChange24hr, percentChange1hr])

table.field_names = ["Coin Name", "Current Price", "Market Cap", "24hr Volume", "24hr percent change", "1hr percent change"]
table.sortby = "24hr percent change"
table.reversesort = True


print(table)
