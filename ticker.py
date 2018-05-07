#!/usr/bin/env python3

import requests
import json

currency ="BTC,ETH,XRP,BCH,EOS,LTC,ADA,TRX,XLM,IOT,BCD,NEO,VEN,DASH,XMR,XEM,BNB,ETC,QTUM,ICX,ZIL,ZRX,HT,LSK,BTG,MITH,IOST,AE,LRC,XVG,NANO,BTM*,ZEC,SNT,NAS"

def ticks(currency):
	url = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(currency)
	response = requests.get(url)
	cryptocompare_json = json.loads(response.text)
	return cryptocompare_json

ticks_json = ticks(currency)

symbols = ["BTC","ETH","XRP","BCH","EOS","LTC","ADA","TRX","XLM","IOT","BCD","NEO","VEN","DASH","XMR","XEM","BNB","ETC","QTUM","ICX","ZIL","ZRX","HT","LSK","BTG","MITH","IOST","AE","LRC","XVG","NANO","BTM*","ZEC","SNT","NAS"]

for symbol in symbols:
	price = ticks_json['RAW'][symbol]['USD']['PRICE']
	changeday = ticks_json['RAW'][symbol]['USD']['CHANGEDAY']

	if changeday > 0:
		print("\x1b[0;33m{}\x1b[0m {} \x1b[0;32m↑\x1b[0m {:.2f}".format(symbol, price, changeday), end="  ")
	else:
		print("\x1b[0;33m{}\x1b[0m {} \x1b[0;31m↓\x1b[0m {:.2f}".format(symbol, price, changeday), end="  ")

print()
