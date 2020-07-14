# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/07/10 13:39
# file_name : __init__.py.py

from appJar import gui

app = gui("SCROLLABLE DEMO", "150x150")

app.startScrollPane("PANE")
for x in range(10):
    for y in range(10):
        name = str(x) + "-" + str(y)
        app.addLabel(name, name, row=x, column=y)
        app.setLabelBg(name, app.RANDOM_COLOUR())
# app.stopScrollPane()
app.go()
