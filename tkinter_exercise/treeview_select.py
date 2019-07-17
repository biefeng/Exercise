from tkinter import *
from tkinter.ttk import Treeview, Style
from tkinter import  messagebox
import requests
import traceback

class My_Tk():
	def __init__(self, root, user_info=None, cookies=None, headers=None):
		self.tk = root
		self.user_info = user_info
		self.base_cookies = cookies
		self.base_headers = headers
		# self.tk.geometry('620x400')
		self.orm = {}
		self.val_map = {}
		self.create_button()
		self.create_heading()
		self.create_tv()

	def create_button(self):
		frame = Frame(self.tk, width=200, height=50)
		frame.pack(fill=X, side=TOP)

		Button(frame, text='增加数据', command=self.download).pack(side=LEFT, anchor='w', padx=26)
		Button(frame, text='测试数据', command=self.insert_test_tree_data).pack(side=LEFT, anchor='w')
		Button(frame, text='清除数据', command=self.clear_tree_data).pack(side=LEFT, anchor='w')

	def get_tv(self):
		return self.tv

	def download(self):
		try:
			for k, v in self.orm.items():
				button = self.orm[k][0]
				button_value = button.getvar(button['variable'])
				if button_value == '1':
					print(self.tv.item(k, 'values'))
					if self.user_info == None:
						pass
					else:
						params = {
							'fragmentId': self.val_map[k],
							'token': self.user_info['token'],
							'albumId': 0,
							'programId': 0
						}
						# self.base_cookies['SERVERID'] = "1ebdc1cc2a3d66d97da2b6d9c90558b4|1563213194|1563213193"
						response = requests.post(url="http://api.dushu.io/fragment/content", json=params,
						                         headers=self.base_headers, cookies=self.base_cookies)
						mediaUrl = response.json()['mediaUrls'][0]
						print(mediaUrl)
						media_info_headers = {
							'Host': "cdn-ali.dushu.io",
							'Cookie': "grwng_uid=e7e51c80-ead6-43bb-9744-7531778d6c73; UM_distinctid=16be039d03e8aa-0f0e963eb0f589-621c740a-4a640-16be039d03f633; gr_user_id=ebc67f00-d109-4c29-80b0-7d631382debf",
							'X-Playback-Session-Id': "D3192900-D956-4460-95F1-C4D28A144B3F",
							'Range': "bytes=0-1",
							'Accept': "*/*",
							'User-Agent': "AppleCoreMedia/1.0.0.16D57 (iPhone; U; CPU OS 12_1_4 like Mac OS X; en_us)",
							'Accept-Language': "en-us",
							'Accept-Encoding': "identity",
							'Connection': "keep-alive",
							'Content-Type': "text/plain",
							'cache-control': "no-cache"
						}
						media_info = requests.get(url=mediaUrl, headers=media_info_headers)
						range_ = media_info.headers['Content-Range']
						content_disposition = media_info.headers['Content-Disposition']
						file_name = content_disposition[content_disposition.rfind('filename='):]
						bytes_length = range_[range_.rfind('/') + 1:]

						with open(r'downloaded.mp4', 'wb') as saved:
							# for i in range(381):
							# 	url = url_prefix + str(i + 1) + url_suffix
							# 	response = requests.get(url=url, headers=headers)
							# 	saved.write(bytes(response.content))
							# 	print("请求到第" + str(i) + "个")
							print("*************start download:" + file_name + "************")
							print(type(bytes_length))
							count = (int(bytes_length) + 1 - 131072) / 131072
							print(count)
							print(type(count))
							for index in range(int(count)):
								if index == count - 1:
									media_info_headers['Range'] = "bytes=" + str(index * 131072) + "-" + str(
										bytes_length)
								else:
									media_info_headers['Range'] = "bytes=" + str(index * 131072) + "-" + str(
										(index + 1) * 131072 - 1)
								media_content = requests.get(url=mediaUrl, headers=media_info_headers)
								saved.write(bytes(media_content.content))
								print("*************downloading************")

						print(self.val_map[k])
		except BaseException as e:
			traceback.print_exc(file=open('error.txt', 'a+'))
			messagebox.showerror("提示", message="下载出错")
			print("下载出错")

	def create_heading(self, ):
		'''重新做一个treeview的头，不然滚动滚动条，看不到原先的头！！！'''
		heading_frame = Frame(self.tk)
		heading_frame.pack(fill=X)

		# 填充用
		# button_frame = Label(heading_frame,bg='gray')
		# button_frame.pack(side=LEFT, expand=False)
		# 全选按钮
		self.all_buttonvar = IntVar()
		self.all_button = Checkbutton(heading_frame, text='', variable=self.all_buttonvar, command=self.select_all)
		self.all_button.pack(side=LEFT)
		self.all_buttonvar.set(0)

		self.columns = ['no', 'name', 'author']
		self.columns_header_name = ['序号', '名称', '作者']
		self.header_label_widths = [40, 260, 100]
		self.colums_header_widths = [46, 292, 115]

		# 重建tree的头
		for i in range(len(self.columns)):
			Label(heading_frame, text=self.columns_header_name[i], width=int(self.header_label_widths[i] * 0.16),
			      anchor='center',
			      relief=GROOVE).pack(side=LEFT)

	def insert_test_tree_data(self):
		rows = []
		for i in range(30):
			rows.append((i + 1, 'B', 'C', 110))
		self.insert_tv(rows)

	def clear_tree_data(self):
		self.init_tree()

	# 初始化表格
	def init_tree(self):
		[self.tv.delete(item) for item in self.tv.get_children()]
		self.tv.update()
		for child in self.button_frame.winfo_children():  # 第一个构件是label，所以忽略
			child.destroy()

		self.canvas.itemconfigure(self.tv_frame, height=300)  # 设定窗口tv_frame的高度
		self.tk.update()
		self.canvas.config(scrollregion=self.canvas.bbox("all"))  # 滚动指定的范围
		self.canvas.config(height=300)

	def create_tv(self):
		# 放置 canvas、滚动条的frame
		canvas_frame = Frame(self.tk, width=500, height=400)
		canvas_frame.pack(fill=X)

		# 只剩Canvas可以放置treeview和按钮，并且跟滚动条配合
		self.canvas = Canvas(canvas_frame, width=400, height=500, scrollregion=(0, 0, 500, 400))
		self.canvas.pack(side=LEFT, fill=BOTH, expand=1)
		# 滚动条
		ysb = Scrollbar(canvas_frame, orient=VERTICAL, command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=ysb.set)
		ysb.pack(side=RIGHT, fill=Y)
		# !!!!=======重点：鼠标滚轮滚动时，改变的页面是canvas 而不是treeview
		self.canvas.bind_all("<MouseWheel>",
		                     lambda event: self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

		# 想要滚动条起效，得在canvas创建一个windows(frame)！！
		tv_frame = Frame(self.canvas)
		self.tv_frame = self.canvas.create_window(0, 0, window=tv_frame, anchor='nw', width=600,
		                                          height=400)  # anchor该窗口在左上方

		# 放置button的frame
		self.button_frame = Frame(tv_frame)
		self.button_frame.pack(side=LEFT, fill=Y)
		Label(self.button_frame, width=3).pack()  # 填充用

		# 创建treeview
		self.tv = Treeview(tv_frame, height=10, columns=self.columns, show='tree')  # height好像设定不了行数，实际由插入的行数决定
		self.tv.column("#0", width=0, stretch=0)
		self.tv.pack(expand=True, side=LEFT, fill=BOTH)
		# 设定每一列的属性
		for i in range(len(self.columns)):
			self.tv.column(self.columns[i], width=self.colums_header_widths[i], anchor='w', stretch=False)

		# 设定treeview格式
		# import tkinter.font as tkFont
		# ft = tkFont.Font(family='Fixdsys', size=20, weight=tkFont.BOLD)
		self.tv.tag_configure('oddrow', font='Arial 8')  # 设定treeview里字体格式font=ft
		self.tv.tag_configure('select', background='SkyBlue', font='Arial 8')  # 当对应的按钮被打勾，那么对于的行背景颜色改变！
		self.rowheight = 27  # 很蛋疼，好像tkinter里只能用整数！
		Style().configure('Treeview', rowheight=self.rowheight)  # 设定每一行的高度

		# 设定选中的每一行字体颜色、背景颜色 (被选中时，没有变化)
		Style().map("Treeview",
		            foreground=[('focus', 'black'), ],
		            background=[('active', 'white')]
		            )
		self.tv.bind('<<TreeviewSelect>>', self.select_tree)  # 绑定tree选中时的回调函数

	def insert_tv(self, rows=None):
		if rows == None:
			rows = []
			for i in range(20):
				item = (i + 1, 'A', "B")
				rows.append(item)

		# 清空tree、checkbutton
		items = self.tv.get_children()
		[self.tv.delete(item) for item in items]
		self.tv.update()
		for child in self.button_frame.winfo_children():  # 第一个构件是label，所以忽略
			child.destroy()

		# 重设tree、button对应关系
		self.orm = {}
		index = 0
		for row in rows:
			tv_item = self.tv.insert('', index, value=row[0:3], tags=('oddrow'))  # item默认状态tags

			import tkinter
			ck_button = tkinter.Checkbutton(self.button_frame, variable=IntVar())
			ck_button['command'] = lambda item=tv_item: self.select_button(item)
			ck_button.pack()
			# ck_button['fragementId']=row[3]
			self.orm[tv_item] = [ck_button]
			self.val_map[tv_item] = row[3]
			index = index + 1

		# 每次点击插入tree，先设定全选按钮不打勾，接着打勾并且调用其函数
		self.all_buttonvar.set(0)
		self.all_button.invoke()

		# 更新canvas的高度
		height = (len(self.tv.get_children()) + 1) * self.rowheight  # treeview实际高度
		self.canvas.itemconfigure(self.tv_frame, height=height)  # 设定窗口tv_frame的高度
		self.tk.update()
		self.canvas.config(scrollregion=self.canvas.bbox("all"))  # 滚动指定的范围
		self.canvas.config(height=height)

	def select_all(self):
		'''全选按钮的回调函数
		   作用：所有多选按钮打勾、tree所有行都改变底色(被选中)'''
		for item, [button] in self.orm.items():
			if self.all_buttonvar.get() == 1:
				button.select()
				self.tv.item(item, tags='select')
			else:
				button.deselect()
				self.tv.item(item, tags='oddrow')

	def select_button(self, item):
		'''多选按钮的回调函数
			作用：1.根据按钮的状态，改变对应item的底色(被选中)
				 2.根据所有按钮被选的情况，修改all_button的状态'''
		button = self.orm[item][0]
		button_value = button.getvar(button['variable'])
		if button_value == '1':
			self.tv.item(item, tags='select')
		else:
			self.tv.item(item, tags='oddrow')
		self.all_button_select()  # 根据所有按钮改变 全选按钮状态

	def select_tree(self, event):
		'''tree绑定的回调函数
		   作用：根据所点击的item改变 对应的按钮'''
		select_item = self.tv.focus()
		button = self.orm[select_item][0]
		button.invoke()  # 改变对应按钮的状态，而且调用其函数

	def all_button_select(self):
		'''根据所有按钮改变 全选按钮状态
			循环所有按钮，当有一个按钮没有被打勾时，全选按钮取消打勾'''
		for [button] in self.orm.values():
			button_value = button.getvar(button['variable'])
			if button_value == '0':
				self.all_buttonvar.set(0)
				break
		else:
			self.all_buttonvar.set(1)


if __name__ == '__main__':
	tk = Tk()
	My_Tk(tk)
	tk.mainloop()
