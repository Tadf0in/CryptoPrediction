import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader as web
import datetime as dt

crypto = 'BTC'
currency = 'EUR'
cryptocurrency = f'{crypto}-{currency}'

start = dt.datetime(2011, 1, 1)
end = dt.datetime.today()

data = web.DataReader(cryptocurrency, 'yahoo', start, end)
prices = data['Close'].values
dates = data['Close'].keys()

# Matplotlib stuff
fig, ax = plt.subplots()
ax.plot(dates, prices, label="Prix officiels")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=12))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.format_xdata = mdates.DateFormatter('%Y-%m')
plt.title(f'Prédiction du prix de {crypto} en {currency}')
plt.xlabel('Temps')
plt.ylabel('Prix')
plt.legend(loc='upper left')
plt.show()