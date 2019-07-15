# -*- coding: utf-8 -*-
__author__ = '33504'

from tkinter import *
from tkinter import ttk

tk = Tk()
tk.geometry("450x500+300+200")

treeview = ttk.Treeview(tk, columns=['no', 'name', 'author'], show='tree headings')

treeview.pack()

treeview.column('#0',stretch=0,width=0)

treeview.column('no', anchor='center',width=150)
treeview.column('name', anchor='center',width=150)
treeview.column('author', anchor='center',width=150)

treeview.heading('no',text='序号')
treeview.heading('name',text='名称')
treeview.heading('author',text='作者')

tk.mainloop()
