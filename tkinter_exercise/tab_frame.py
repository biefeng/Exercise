# -*- coding: utf-8 -*-
__author__ = '33504'

# !/usr/bin/env python
# -*- coding:utf-8 -*-

import os, sys
from tkinter_exercise.DownLoaUtil import application as main_page

if sys.version_info[0] == 2:
    from tkinter import *
    from tkinter.font import Font
    from tkinter.ttk import *
    # Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkinter.messagebox import *
# Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
# import tkFileDialog
# import tkSimpleDialog
else:  # Python 3.x
    from tkinter import *
    from tkinter.font import Font
    from tkinter_exercise.tasklist import tasklist as tasklist
    from tkinter.ttk import Notebook, Style, Treeview
    from tkinter.messagebox import *


# import tkinter.filedialog as tkFileDialog
# import tkinter.simpledialog as tkSimpleDialog    #askstring()


class Application_ui(Frame):
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Form1')
        self.master.geometry('850x650+400+250')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.TabStrip1 = Notebook(self.top, takefocus='red')
        print(type(self.TabStrip1['takefocus']))
        self.TabStrip1.place(relx=0.02, rely=0.005, relwidth=0.96, relheight=0.99)

        self.TabStrip1__Tab2 = Frame(self.TabStrip1, bg='white')
        tasklist_ = tasklist()
        tasklist_.create_tasklist_tv(self.TabStrip1__Tab2)

        self.TabStrip1__Tab1 = Frame(self.TabStrip1)
        self.home = main_page(self.TabStrip1__Tab1, tasklist_)
        self.TabStrip1.add(self.TabStrip1__Tab1, text='首页')

        self.TabStrip1.add(self.TabStrip1__Tab2, text='任务列表')

    def create_tasklist_tv(self, tv):
        canvas_frame = Frame(tv, width=500, height=400)
        canvas_frame.pack(fill=X)

        treeview = self.TabStrip1__Tab2Lbl = Treeview(tv, columns=("no", "name"))
        treeview.column("#0", width="0", stretch=0)
        treeview.column("no", width="10")
        treeview.column("name", width="200")

        treeview.heading("no", text="序号")
        treeview.heading("name", text="名称")

        self.TabStrip1__Tab2Lbl.place(relx=0.02, rely=0.005, relwidth=0.76, relheight=0.99)
        progress_frame = self.progress_frame = Frame(tv)
        progress_frame.place(relwidth=0.2, relheight=0.99, relx=0.79, rely=0.005)
        progress_head = Label(progress_frame, bg="white", text="进度")
        progress_head.pack(side=TOP, fill=X)
        self.TabStrip1.add(self.TabStrip1__Tab2, text='任务列表')

    def insert_data(self):
        treeview = self.TabStrip1__Tab2Lbl
        treeview.insert("", 1, value=("1", "你好"))
        treeview.insert("", 2, value=("2", "你好"))
        treeview.insert("", 3, value=("3", "你好"))
        treeview.insert("", 4, value=("4", "你好"))
        treeview.insert("", 5, value=("5", "你好"))
        treeview.insert("", 6, value=("6", "你好"))
        treeview.insert("", 7, value=("7", "你好"))
        treeview.insert("", 8, value=("8", "你好"))
        treeview.insert("", 9, value=("9", "你好"))
        treeview.insert("", 10, value=("10", "你好"))
        treeview.insert("", 11, value=("11", "你好"))
        treeview.insert("", 12, value=("12", "你好"))
        treeview.insert("", 13, value=("13", "你好"))
        treeview.insert("", 14, value=("14", "你好"))
        treeview.insert("", 15, value=("15", "你好"))
        treeview.insert("", 16, value=("16", "你好"))
        treeview.insert("", 17, value=("17", "你好"))
        treeview.insert("", 18, value=("18", "你好"))
        treeview.insert("", 19, value=("19", "你好"))
        treeview.insert("", 20, value=("20", "你好"))
        treeview.insert("", 21, value=("21", "你好"))
        treeview.insert("", 22, value=("22", "你好"))
        treeview.insert("", 23, value=("23", "你好"))
        treeview.insert("", 24, value=("24", "你好"))
        treeview.insert("", 25, value=("25", "你好"))
        treeview.insert("", 26, value=("26", "你好"))
        treeview.insert("", 27, value=("27", "你好"))

        progress = Label(self.progress_frame, bg="white", text="100%")
        progress.pack(side=TOP, fill=X)
        width_ = 200
        canvas = Canvas(progress, width=width_, height=10, bg="white")
        canvas.place(relx=0, rely=0)


class Application(Application_ui):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)


if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
