import requests
from openpyxl import Workbook
import datetime

# Set up my API authentication:
api = 'https://api.coinmarketcap.com/v2/ticker/'

raw_data = requests.get(api).json()

data = raw_data['data']
# save requested raw api data down

today = datetime.date.today()

file = Workbook()
sheet = file.create_sheet(str(today), 0)


# iterate through the data to find the neccessary keys that I want:
for currency in data:
    sheet.append([
        data[currency]['name'],
        data[currency]['quotes']['USD']['price'],
        data[currency] ['quotes']['USD']['market_cap'],
        data[currency]['quotes']['USD']['volume_24h'],
        data[currency]['quotes']['USD']['percent_change_1h'],
        data[currency]['quotes']['USD']['percent_change_24h']
        ])

file.save('CurrencyAnalysis.xlsx')
