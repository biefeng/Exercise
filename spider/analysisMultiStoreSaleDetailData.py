# -*- coding: utf-8 -*-
__author__ = '33504'

import matplotlib.dates as dates
import matplotlib.pyplot as plt
import pandas as pd
import json
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

df = pd.read_csv(r"sale_detail_11_04.csv", delimiter=r" ",
                 usecols=lambda x: x in ['createDateStr', 'amount', 'storeName'])
df.amount = df["amount"].apply(pd.to_numeric, errors="coerce").fillna(0.0)
df.createDateStr = pd.to_datetime(df.createDateStr, errors='coerce').dt.date

fig = plt.figure(figsize=(25, 10))
fig.set_tight_layout(True)

plt.title("店铺台账")

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.xlabel("日期")
plt.ylabel("金额")

_data = {}
for _store_name, _group in df.groupby("storeName"):
    data = {}
    for name, group in _group.groupby("createDateStr"):
        print(name)
        if len(group.sum().values) == 2:
            data[name] = group.sum().values[0]
    _data[_store_name] = data
# print(json.dumps(_data))
_stores = []
_dates = None
for _k, _v in _data.items():
    if _dates is None:
        _dates = list(_v.keys())
    plt.plot(_dates, list(_v.values()), marker='o', markersize=3)
    _stores.append(_k)
    for _x, _y in zip(list(_v.keys()), list(_v.values())):
        plt.text(_x, _y, _y, ha='center', va='bottom', fontsize=10)
plt.legend(_stores)
ax = plt.gca()
ax.xaxis.set_major_formatter(dates.DateFormatter("%m/%d"))
plt.show()
