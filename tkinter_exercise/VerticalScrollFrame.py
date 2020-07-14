# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/07/10 11:49
# file_name : VerticalScrollFrame.py

from tkinter import *
import tkinter.ttk as ttk

import tkinter as tk
from tkinter.ttk import Treeview
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('500x200')
style = ttk.Style(root)
style.configure('Treeview', rowheight=40)  #SOLUTION
tree = ttk.Treeview(root)
tree.insert('', 0, text='Line 1 of many XXX', tags='T')
tree.insert('', 1, text='Line 2 of many XXX', tags='T')
tree.insert('', 2, text='Line 3 of many XXX', tags='T')
tree.column('#0', stretch=True)
tree.tag_configure('T', font='Arial 20')
tree.pack(fill='x')
root.mainloop()