import code
import datetime
import os
import os.path
import csv
import tkinter as tk

from collections import OrderedDict
from pandas_datareader import data
from datetime import date, timedelta

symbols = ['AAPL', 'MSFT']
#window = tkinter.Tk()
#my_message = tkinter.Message(text="Hi. Welcome to my Example GUI Application!", width=1000)

# ENTRY (TEXT INPUT) WITH LABEL
def handle_button_click():
    ticker = my_entry.get()
    print(ticker)
    return(ticker)


#my_label = tkinter.Label(text="Input Ticker Here:")
#entry_value = tkinter.StringVar()
#my_entry = tkinter.Entry(textvariable=entry_value)
#my_label.pack()
#my_entry.pack()
#my_button = tkinter.Button(text="Click Me", command=handle_button_click)
#my_button.pack()

#print(my_button)

#my_message.pack()
class SampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        ticker_label = tk.Label(text="Ticker").pack(side="left")
        self.entry = tk.Entry(self)
        self.entry.pack(side="left")

        date_label = tk.Label(text="Date").pack(side="left")
        self.date_entry = tk.Entry(self)
        self.date_entry.pack(side="left")

        #self.entry_date = tk.Entry(self,"date")

        self.button = tk.Button(self, text="Get", command=self.on_button)
        self.button.pack()
        self.tickers = []
        self.start = str(date.today() - timedelta(days=15)) #> '2017-07-09'
        self.end = str(date.today()) #> '2017-07-24'
        self.data_source = 'google'
        self.label = tk.Label(text = "")
        self.label.pack()

    def on_button(self):
        self.tickers = []
        self.tickers.append(self.entry.get())
        s = self.date_entry.get()
        slist = s.split("-")
        sdate = datetime.date(int(slist[0]),int(slist[1]),int(slist[2]))
        self.start = sdate
        self.end = sdate
        response = data.DataReader(self.tickers, self.data_source, self.start, self.end)
        daily_closing_prices = response.ix["Close"] # ix() is a pandas DataFrame function
        self.label.destroy()
        self.label = tk.Label(text = "Prices are:\n" + str(daily_closing_prices))
        self.label.pack(side="bottom")
        print(daily_closing_prices)

w = SampleApp()
w.mainloop()
