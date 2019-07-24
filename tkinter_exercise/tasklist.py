# -*- coding: utf-8 -*-
__author__ = '33504'

from tkinter.ttk import Treeview, Style
from tkinter import *
import time


class tasklist:

	def __init__(self):
		self.index=1
		self.rows={}

	def test(self):
		lineheight = 25
		height = lineheight * 21
		self.canvas.itemconfigure(self.canvas_create_window, height=height)
		print(self.canvas.bbox('all'))
		self.canvas.config(scrollregion=self.canvas.bbox('all'))
		self.tv.update()
		print(self.canvas)
		for i in range(20):
			self.insert_data(("1","第三选择",self.catch_progress_bar()))
			print("index: " + str(i))
		print("finished")

	def catch_progress_bar(self):
		progress_bar = Frame(self.progress_bar_frame, bg="orange")
		canvas = Canvas(progress_bar, width=235, height=19, bg='grey')
		return canvas

	def insert_data(self, row):
		self.rows[row[0]]=row
		index = Label(self.index_frame, text=self.index, height=1, bg='orange')
		index.pack(side=TOP, pady=0.5, fill=X)

		name = Label(self.name_frame, text=row[1], bg="orange")
		name.pack(side=TOP, pady=0.5, fill=X)

		self.progress_bar = Frame(self.progress_bar_frame, bg="orange")
		self.progress_bar.pack(side=TOP, pady=0.5, fill=X)

		canvas = Canvas(self.progress_bar, width=235, height=19, bg='white')
		canvas.pack(side=TOP, expand=True, fill=BOTH)

		self.index=self.index+1

		x = 300
		n = 220 / x
		for i in range(x):
			n = n + (220 / x)
			self.progress(canvas, n)

	def progress(self, bar, n):
		fill_line = bar.create_rectangle(10, 10, 2, 10, width=0, fill='green')
		bar.coords(fill_line, (0, 0, n, 60))
		self.tv.update()

	def create_tasklist_tv(self, tv):
		self.tv = tv
		button = Button(tv, text="test", command=self.test)
		button.place(x=10, y=10)

		header_frame = Frame(tv,bg="white")
		header_frame.place(relx=0.032, rely=0.37, relwidth=0.906, height=20)

		progress_bar_head = Label(header_frame, text="序号", bg="white", bd=2, relief=RIDGE, anchor="center")
		# progress_bar_head.pack(side=LEFT, fill=BOTH)
		progress_bar_head.place(relx=0.002, rely=0.005, relwidth=0.157, relheight=0.99)

		progress_bar_head = Label(header_frame, text="名称", bd=2, relief=RIDGE, anchor="center")
		progress_bar_head.place(relx=0.158, rely=0.005, relwidth=0.52, relheight=0.99)

		progress_bar_head = Label(header_frame, text="进度", bd=2, relief=RIDGE, anchor="center")
		progress_bar_head.place(relx=0.676, rely=0.005, relwidth=0.308, relheight=0.99)

		canvas = self.canvas = Canvas(tv, width=800, height=300, scrollregion=(0, 0, 800, 300))  # 创建canvas
		canvas.place(x=10, y=250)  # 放置canvas的位置
		frame = Frame(canvas)  # 把frame放在canvas里
		frame.place(width=760, height=300)  # frame的长宽，和canvas差不多的

		vbar = Scrollbar(canvas, orient=VERTICAL, bg="red", troughcolor="red")  # 竖直滚动条
		vbar.place(x=770, y=0, width=10, height=300)
		vbar.configure(command=canvas.yview)

		canvas.config(yscrollcommand=vbar.set)  # 设置
		self.canvas_create_window = canvas.create_window(0, 0, window=frame, anchor="nw", width=760, height=300)

		canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

		# *****************************

		self.index_frame = Frame(frame, bd=2, relief=RIDGE)
		self.index_frame.place(relx=0.02, rely=0.005, relwidth=0.15, relheight=0.99)

		self.name_frame = Frame(frame, bd=2, relief=RIDGE)
		self.name_frame.place(relx=0.167, rely=0.005, relwidth=0.52, relheight=0.99)

		self.progress_bar_frame = Frame(frame, bd=2, relief=RIDGE)
		self.progress_bar_frame.place(relx=0.673, rely=0.005, relwidth=0.3, relheight=0.99)



if __name__=='__main__':
	win = Tk()
	win.geometry("800x600+200+50")
	win.title("任务列表")
	t = tasklist()
	t.create_tasklist_tv(win)

	win.mainloop()
