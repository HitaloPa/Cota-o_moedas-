import json
import requests 
#TODO Make this Object Orientated
#TODO Make a Graphic interface with Tkinter
ex_rate = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
ex_rate = ex_rate.json()

#print(ex_rate)
dolar_rate = float(ex_rate['USDBRL']['bid'])
euro_rate = float(ex_rate['EURBRL']['bid'])
bitcoin_rate = float(ex_rate['BTCBRL']['bid'])
print(f"O dolar esta custando R${round(dolar_rate,2)}")
print(f"O euro esta custando R${round(euro_rate,2)}")
print(f"O Bitcoin esta custando R${round(bitcoin_rate,2)}")