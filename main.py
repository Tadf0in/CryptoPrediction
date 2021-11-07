import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader as web
import datetime as dt

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

crypto = 'BTC'
currency = 'EUR'
cryptocurrency = f'{crypto}-{currency}'

start = dt.datetime(2011, 1, 1)
end = dt.datetime.today()

data = web.DataReader(cryptocurrency, 'yahoo', start, end)
prices = data['Close'].values
dates = data['Close'].keys()
# Scaling prices between 0 and 1 with 0 = 0€ and 1 = maximum price
max_price = max(prices)
for i in range(len(prices)):
    prices[i] = prices[i] / max_price

days = 61 # 2 months

x, y = [], []
for i in range(days, len(prices)):
    x.append(prices[i-days:i]) # Stock all prices between day n°i and day n°i - 2 months
    y.append(prices[i]) # Stock price at day n°i

x, y = np.array(x), np.array(y)
x = np.reshape(x, (x.shape[0], x.shape[1], 1))
"""
x :
[
    [
        [0 < price < 1],
        [0 < price < 1],
        ... lenght = days
    ],
    [
        [0 < price < 1],
        [0 < price < 1],
        ... lenght = days
    ],
    ... lenght = len(data) - days
]
y : [0 < price < 1, 0 < price < 1, ...]

dataset : (x[[i]] (list of n past days) with n = days, y[i])

model : 
"""
model = keras.Sequential(
    [
        layers.Dense(2, activation="relu"),
        layers.Dense(3, activation="relu"),
        layers.Dense(4),
    ]
)




# Recreating real prices
for i in range(len(prices)):
    prices[i] = prices[i] * max_price
    
# Matplotlib stuff
fig, ax = plt.subplots()
ax.plot(dates, prices, label="Prix officiels")
ax.plot(dates[days:], y)

ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')

plt.title(f'Prédiction du prix de {crypto} en {currency}')
plt.xlabel('Temps')
plt.ylabel('Prix')
plt.legend(loc='upper left')
plt.show()
