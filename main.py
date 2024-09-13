import requests
from tkinter import *
import pandas as pd

#TODO Make this Object Orientated
#TODO Make a Graphic interface with Tkinter


#Requesting the API awesomeapi.com the last Exchage rate for Dolar to real,Euro to real and Bicoin to real and tranforming it from json to a Dictionary and returning it.
def Exange_R():
    ex_rate = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    ex_rate = ex_rate.json()
    return ex_rate

#Reciving the data from the Dictionary and retriving the value of the Dolar
def Dolar():
    ex_rate = Exange_R()
    dolar_rate = float(ex_rate['USDBRL']['bid'])
    txt=f'O Dolar esta custando R${round(dolar_rate,2)}'
    txt_asw["text"]=txt
    return dolar_rate
    
#Reciving the data from the Dictionary and retriving the value of the Euro
def Euro():
    ex_rate = Exange_R()
    euro_rate = float(ex_rate['EURBRL']['bid'])
    txt=f'O Euro esta custando R${round(euro_rate,2)}'
    txt_asw["text"]=txt
    return euro_rate
    
#Reciving the data from the Dictionary and retriving the value of the Bitcoin
def Bitcoin():
    ex_rate = Exange_R()
    bitcoin_rate = float(ex_rate['BTCBRL']['bid'])
    txt=f'O Bitcoin esta custando R${round(bitcoin_rate,2)}'
    txt_asw["text"]=txt
    return bitcoin_rate



window = Tk()
window.title('Currency Exchange Rate')
window.geometry('400x400')

#cheating a text to show in the window
txt = Label(window,text="Selecion para apresentar dados")
txt.grid(column=0,row=0,columnspan=3,padx=10,pady=10)


#creating buttons and comunicating with the methods 
btn1=Button(window,text="DOLAR",command=Dolar)
btn1.grid(column=0,row=2,padx=10,pady=10)

btn2=Button(window,text="EURO",command=Euro)
btn2.grid(column=1,row=2,padx=10,pady=10)

btn3=Button(window,text="BITCOIN",command=Bitcoin)
btn3.grid(column=2,row=2,padx=10,pady=10)

#text answer from the methods
txt_asw=Label(window,text="")
txt_asw.grid(column=0,row=3,columnspan=3)

#closing the window loop
window.mainloop()


