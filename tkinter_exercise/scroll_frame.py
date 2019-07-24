# -*- coding: utf-8 -*-
__author__ = '33504'

from tkinter import *

win = Tk()
win.geometry("800x600+200+50")
canvas = Canvas(win, width=200, height=180, scrollregion=(0, 0, 520, 520))  # 创建canvas
canvas.place(x=75, y=265)  # 放置canvas的位置
frame = Frame(canvas)  # 把frame放在canvas里
frame.place(width=180, height=180)  # frame的长宽，和canvas差不多的
vbar = Scrollbar(canvas, orient=VERTICAL)  # 竖直滚动条
vbar.place(x=180, width=20, height=180)
vbar.configure(command=canvas.yview)
hbar = Scrollbar(canvas, orient=HORIZONTAL)  # 水平滚动条
hbar.place(x=0, y=165, width=180, height=20)
hbar.configure(command=canvas.xview)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)  # 设置
canvas.create_window(0,0, window=frame,anchor="nw")  # create_window

label = Label(frame, text="123")
label.pack(side=TOP)

label1 = Label(frame, text="234")
label1.pack(side=TOP)


labe2 = Label(frame, text="345")
labe2.pack(side=TOP)


labe3 = Label(frame, text="345")
labe3.pack(side=TOP)

win.mainloop()
