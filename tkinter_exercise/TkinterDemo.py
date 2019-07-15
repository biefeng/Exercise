# -*- coding: utf-8 -*-
__author__ = '33504'

from tkinter import *
from tkinter import ttk

win = Tk()
win.title("yudanqu")
win.geometry("800x600+600+250")
# win.state("zoomed")


# 搜索
search_frame = Frame(win)
search_frame.pack()

search_label = Label(search_frame, text="搜索:", bg=None, fg="black", font=("黑体", 12), width=7, height=2, wraplength=1000,
                     justify="left", anchor="center")
e = Variable()
search_input = Entry(search_frame, textvariable=e, width=50)

search_button = Button(search_frame, text="搜索")

search_label.grid(column=1, row=1)
search_input.grid(column=2, row=1)
search_button.grid(column=3, padx=20, row=1)

# 表格
tree = ttk.Treeview(win, show="headings", padding=LEFT)
tree.pack(fill=BOTH, side=BOTTOM)

# 定义列
tree["columns"] = ("no", "name", "time")
# 设置列，列还不显示
tree.column("no", width=100, anchor='center')
tree.column("name", width=100, anchor='center')
tree.column("time", width=100, anchor='center')

# 设置表头
tree.heading("no", text="序号")
tree.heading("name", text="名称")
tree.heading("time", text="时长")

# 添加数据
tree.insert("", 0, values=("小郑", "34", "177cm"))
tree.insert("", 1, values=("小张", "43", "188cm"))
win.mainloop()
