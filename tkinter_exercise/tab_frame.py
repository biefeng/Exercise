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
	from tkinter.ttk import Notebook, Style
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

		self.TabStrip1 = Notebook(self.top,takefocus='red')
		print(type(self.TabStrip1['takefocus']))
		self.TabStrip1.place(relx=0.02, rely=0.005, relwidth=0.96, relheight=0.99)

		self.TabStrip1__Tab1 = Frame(self.TabStrip1)
		self.home = main_page(self.TabStrip1__Tab1)
		self.TabStrip1.add(self.TabStrip1__Tab1, text='首页')

		# self.TabStrip1__Tab2 = Frame(self.TabStrip1)
		# self.TabStrip1__Tab2Lbl = Label(self.TabStrip1__Tab2, text='Please add widgets in code.')
		# self.TabStrip1__Tab2Lbl.place(relx=0.1, rely=0.5)
		# self.TabStrip1.add(self.TabStrip1__Tab2, text='任务列表')
		#
		# self.TabStrip1__Tab2 = Frame(self.TabStrip1)
		# self.TabStrip1__Tab2Lbl = Label(self.TabStrip1__Tab2, text='Please add widgets in code.')
		# self.TabStrip1__Tab2Lbl.place(relx=0.1, rely=0.5)
		# self.TabStrip1.add(self.TabStrip1__Tab2, text='下载设置')


class Application(Application_ui):
	# 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
	def __init__(self, master=None):
		Application_ui.__init__(self, master)


if __name__ == "__main__":
	top = Tk()
	Application(top).mainloop()
