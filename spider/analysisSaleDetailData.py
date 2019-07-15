# -*- coding: utf-8 -*-
__author__ = '33504'

from datetime import date

import matplotlib.dates as dates
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(fr"H:\workspace\pycharm\Exercise\spider\sale_detail.csv", delimiter=r" ",
                 usecols=lambda x: x in ['createDateStr', 'pin'])

df.createDateStr = pd.to_datetime(df.createDateStr).dt.date

data = {}
for name, group in df[df.createDateStr > date(2019, 6, 5)].groupby('createDateStr'):
	data[name] = group.sum().values[0]

# d = dict({str(name): group.sum().values[0]})
plt.plot(list(data.keys()), list(data.values()))
ax = plt.gca()
ax.xaxis.set_major_locator(dates.WeekdayLocator(byweekday=5))
ax.xaxis.set_major_formatter(dates.DateFormatter("%m/%d/"))
plt.show()
