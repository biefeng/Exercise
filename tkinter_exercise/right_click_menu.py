# -*- coding: utf-8 -*-
__author__ = '33504'

import tkinter

win = tkinter.Tk()
win.title("yudanqu")
win.geometry("400x400+200+50")

# 菜单条
menubar = tkinter.Menu(win)

def func():
 print("**********")

# 菜单
menu = tkinter.Menu(menubar, tearoff=False)
# 给菜单选项添加内容
for item in ['python','c','java','c++', 'c#','php','B','退出']:
 if item == '退出':
     # 添加分割线
     menu.add_separator()
     menu.add_command(label=item, command=win.quit)
 else:
     menu.add_command(label=item, command=func)

menubar.add_cascade(label="语言", menu=menu)
menubar.add_cascade(label="label")

def showMenu(event):
 menubar.post(event.x_root, event.y_root)

win.bind("<Button-3>", showMenu)

win.mainloop()