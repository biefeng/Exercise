# -*- coding: utf-8 -*-
__author__ = '33504'

from datetime import date, datetime

import matplotlib.dates as dates
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

df = pd.read_csv(r"sale_detail_6_2.csv", delimiter=r" ",
                 usecols=lambda x: x in ['createDateStr', 'amount'])
df.amount = df["amount"].apply(pd.to_numeric, errors="coerce").fillna(0.0)
df.createDateStr = pd.to_datetime(df.createDateStr, errors='coerce').dt.date

df.head()
data = {}
for name, group in df[df.createDateStr > date(2019, 6, 6)][df.createDateStr < date(2020, 6, 1)].groupby(
        'createDateStr'):
    print(name)
    if len(group.sum().values) == 1:
        data[name] = group.sum().values[0]
        print(group.sum().values[0])

# d = dict({str(name): group.sum().values[0]})

fig = plt.figure(figsize=(25, 10))
fig.set_tight_layout(True)

plt.plot(list(data.keys()), list(data.values()))
ax = plt.gca()
ax.grid(axis='y', alpha=.9, color="gray", linestyle='-.')

ax.xaxis.set_major_locator(dates.DayLocator(interval=10))
ax.xaxis.set_major_formatter(dates.DateFormatter("%m%d/"))
plt.show()
#
# fig = plt.figure()
# fig.add_subplot()
# fig.set_tight_layout(True)
