#!/usr/bin/env python3

import requests
import json

def ticks(currency):
	url = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(currency)
	response = requests.get(url)
	cryptocompare_json = json.loads(response.text)
	return cryptocompare_json

def yellow(x): return "\x1b[33m"+x+"\x1b[0m"
def bold(x): return "\x1b[1m"+x+"\x1b[0m" 

symbols = [
	"BTC","ETH","XRP","BCH","EOS","LTC","ADA","TRX","XLM","IOT","BCD","NEO",
	"VEN","DASH","XMR","XEM","BNB","ETC","QTUM","ICX","ZIL","ZRX","HT","LSK",
	"BTG","MITH","IOST","AE","LRC","XVG","NANO","BTM*","ZEC","SNT","NAS"
]

currency = ",".join(symbols)
ticks_json = ticks(currency)

bull = "\x1b[32m↑\x1b[0m"
bear = "\x1b[31m↓\x1b[0m"

for symbol in symbols:
	price = ticks_json['RAW'][symbol]['USD']['PRICE']
	changeday = ticks_json['RAW'][symbol]['USD']['CHANGEDAY']
	pprice = str(round(price, 2))
	pchangeday = str(round(changeday, 2))

	if changeday > 0:
		print("{} {} {} {}".format(bold(symbol), yellow(pprice), bull, pchangeday), end="  ")
	else:
		print("{} {} {} {}".format(bold(symbol), yellow(pprice), bear, pchangeday), end="  ")

print()
