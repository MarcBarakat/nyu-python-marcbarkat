import code
import datetime
import os
import os.path
import csv
import tkinter as tk

from collections import OrderedDict
from pandas_datareader import data
from datetime import date, timedelta
class PriceApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        ticker_label = tk.Label(text="Ticker").pack(side="left")
        self.entry = tk.Entry(self)
        self.entry.pack(side="left")

        date_label = tk.Label(text="Start Date (YYYY-MM-DD)").pack(side="left")
        self.date_entry = tk.Entry(self)
        self.date_entry.pack(side="left")

        end_date_label = tk.Label(text="End Date (YYYY-MM-DD)").pack(side="left")
        self.end_date_entry = tk.Entry(self)
        self.end_date_entry.pack(side="left")

        self.tickers = []
        self.start = str(date.today() - timedelta(days=15)) #> '2017-07-09'
        self.end = str(date.today()) #> '2017-07-24'
        self.data_source = 'google'
        self.label = tk.Label(text = "")
        self.label.pack()
        self.button = tk.Button(self, text="Get Price Stats", command=self.on_button)
        self.button.pack(side="top")

    @staticmethod
    def date_from_str(str_date):
        slist = str_date.split("-")
        sdate = datetime.date(int(slist[0]),int(slist[1]),int(slist[2]))
        return(sdate)


    def on_button(self):
        self.tickers = []
        self.tickers.append(self.entry.get())
        self.start = PriceApp.date_from_str(self.date_entry.get())
        self.end = PriceApp.date_from_str(self.end_date_entry.get())
        response = data.DataReader(self.tickers, self.data_source, self.start, self.end)
        daily_closing_prices = response.ix["Close"] # ix() is a pandas DataFrame function
        self.label.destroy()

        if daily_closing_prices.empty:
            self.label = tk.Label(text = "Invalid ticker and/or dates please verify values \n")
        else:
            self.label = tk.Label(text = "Summary Stats are: \n" + str(daily_closing_prices.describe()) + "\nLatest value is:\n" + str(daily_closing_prices[-1:]))

        self.label.pack(side="bottom")
        print(daily_closing_prices)

w = PriceApp()
w.mainloop()
