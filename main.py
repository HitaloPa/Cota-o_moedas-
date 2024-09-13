import json
import requests 
#TODO Make this Object Orientated
#TODO Make a Graphic interface with Tkinter
ex_rate = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
ex_rate = ex_rate.json()

#print(ex_rate)
dolar_rate = float(ex_rate['USDBRL']['bid'])
print(f"O dolar esta custando R${round(dolar_rate,2)}")

