import requests
from prettytable import PrettyTable
import time
import subprocess

# load api data information:
api = "https://api.binance.com/api/v1/ticker/allPrices"
data = requests.get(api).json()

# containers for storing data
symbols = []
positions = []

for x in range(len(data)):
    if('BTC' in data[x]['symbol']):
        positions.append(x)
        symbols.append(data[x]['symbol'])

table = PrettyTable()
table.field_names = ["Symbol", "Change"]

counter = 12
up_change = 0.75
down_change = -0.75
alert_change = 1.5

prices = [[0 for x in range(0)] for y in range(len(symbols))]

while(True):

    has_rows = False
    play_alert = False
    data = requests.get(api).json()
    i = 0

    for x in positions:
        if(len(prices[i]) > counter):
            prices[i].pop(0)
        prices[i].append(data[x]['price'])

        if((float(prices[i][-1]) > float(prices[i][0]) * (1 + up_change / 100) or float(prices[i][-1]) < float(prices[i][0]) * (1 + down_change / 100))):
            current_symbol = symbols[i]
            current_price = round(float(prices[i][-1]) * 100/float(prices[i][0]) - 100, 2)
            table.add_row([current_symbol, current_price])
            has_rows = True

            if(current_price > alert_change):
                play_alert = True
        i += 1

    if (has_rows == True):
        table.sortby = "Change"
        table.reversesort = True

        print(" ")
        print("----" + time.strftime('%X') + " ----")
        print(table)

    if (play_alert == True):
        subprocess.call(["afplay", "dit.wav"])

    table.clear_rows()

    time.sleep
