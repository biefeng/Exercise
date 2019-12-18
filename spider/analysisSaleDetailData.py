# -*- coding: utf-8 -*-
__author__ = '33504'

from datetime import date

import matplotlib.dates as dates
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv(r"sale_detail.csv", delimiter=r" ",
                 usecols=lambda x: x in ['createDateStr', 'amount'])

df.createDateStr = pd.to_datetime(df.createDateStr).dt.date

data = {}
for name, group in df[df.createDateStr > date(2019, 6, 5)].groupby('createDateStr'):
	print(name)
	data[name] = group.sum().values[0]

# d = dict({str(name): group.sum().values[0]})
print(data)
plt.plot(list(data.keys()), list(data.values()))
ax = plt.gca()
ax.xaxis.set_major_locator(dates.WeekdayLocator())
ax.xaxis.set_major_formatter(dates.DateFormatter("%m%d/"))
plt.show()
