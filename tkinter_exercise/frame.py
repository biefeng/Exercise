# -*- coding: utf-8 -*-
__author__ = '33504'

import tkinter

win = tkinter.Tk()
win.title("yudanqu")
win.geometry("400x400+200+50")

'''
框架控件：在桌面上显示一个矩形区域，多作为一个容器控件
'''

frm = tkinter.Frame(win)
frm.pack()

# left
frm_l = tkinter.Frame(frm,bg='red')
tkinter.Label(frm_l, text="左上", bg="pink").pack(side=tkinter.LEFT)
tkinter.Label(frm_l, text="左下", bg="blue").pack(side=tkinter.LEFT)
frm_l.pack(side=tkinter.LEFT)

# right
frm_r = tkinter.Frame(frm)
tkinter.Label(frm_r, text="右上", bg="green").pack(side=tkinter.TOP)
tkinter.Label(frm_r, text="右下", bg="yellow").pack(side=tkinter.TOP)
frm_r.pack(side=tkinter.RIGHT)

win.mainloop()