import requests 
from tkinter import *
#TODO Make this Object Orientated
#TODO Make a Graphic interface with Tkinter

def Exange_R():
    ex_rate = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    ex_rate = ex_rate.json()
    return ex_rate
def Dolar():
    ex_rate = Exange_R()
    dolar_rate = float(ex_rate['USDBRL']['bid'])
    txt=f'O dolar esta custando R${round(dolar_rate,2)}'
    txt_asw["text"]=txt
    
    
def Euro():
    ex_rate = Exange_R()
    euro_rate = float(ex_rate['EURBRL']['bid'])
    txt=f'O EUro esta custando R${round(euro_rate,2)}'
    txt_asw["text"]=txt
    
def Bitcoin():
    ex_rate = Exange_R()
    bitcoin_rate = float(ex_rate['BTCBRL']['bid'])
    txt=f'O Bitcoin esta custando R${round(bitcoin_rate,2)}'
    txt_asw["text"]=txt
    


window = Tk()
window.title('Currency Exchange Rate')
txt = Label(window,text="Selecion para apresentar dados")
txt.grid(column=1,row=0)

btn1=Button(window,text="DOLAR",command=Dolar)
btn1.grid(column=0,row=2)

btn2=Button(window,text="EURO",command=Euro)
btn2.grid(column=1,row=2)

btn3=Button(window,text="BITCOIN",command=Bitcoin)
btn3.grid(column=2,row=2)

txt_asw=Label(window,text="")
txt_asw.grid(column=1,row=3)
window.mainloop()