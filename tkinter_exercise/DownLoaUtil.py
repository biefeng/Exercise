# -*- coding: utf-8 -*-
import requests
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from io import BytesIO
from tkinter_exercise.treeview_select import My_Tk

#
# base_headers = {
#
# 	'Host': 'api.dushu.io',
# 	'Accept': '*/*',
# 	'Accept - Language': 'en - CN;q = 1, zh - Hans - CN;q = 0.9, zh - Hant - CN;q = 0.8',
# 	'Accept - Encoding': 'br, gzip, deflate',
# 	'User - Agent': 'bookclub / 3.9.46(iPhone;iOS12.1.4;Scale / 3.00)',
# }
base_headers = {
	'Accept': "*/*",
	'X-DUSHU-APP-VER': "3.9.46",
	'X-DUSHU-APP-PLT': "1",
	'Accept-Language': "en-CN;q=1, zh-Hans-CN;q=0.9, zh-Hant-CN;q=0.8",
	'X-DUSHU-APP-MUID': "A2E139A0-FDA6-49F4-A40B-A9A8E2CF049F",
	'Accept-Encoding': "br, gzip, deflate",
	'Content-Type': "application/json; charset=utf-8",
	'User-Agent': "bookclub/3.9.46 (iPhone; iOS 12.1.4; Scale/3.00)",
	'Connection': "keep-alive",
	'X-DUSHU-APP-SYSVER': "Version 12.1.4 (Build 16D57)",
	'X-DUSHU-APP-DEVID': "FD797288-5821-4A8B-9C21-187365BF8996",
	'X-DUSHU-APP-DEVTOKEN': "d870663f9e3d09db02a987d58050b108db2cc0246f83144cbc19a82454fc4b48",
	'cache-control': "no-cache",
}

base_cookies = {
	'grwng_uid': 'e7e51c80-ead6-43bb-9744-7531778d6c73',
	'UM_distinctid': '16be039d03e8aa-0f0e963eb0f589-621c740a-4a640-16be039d03f633',
	'gr_user_id': 'ebc67f00-d109-4c29-80b0-7d631382debf'


}


class application:
	def __init__(self, root,tasklist_):
		self.root = root
		self.api_uri = r"http://api.dushu.io"
		self.gateway_url = r"http://gateway-api.dushu.io"
		self.user = {}
		self.req_prop = {}
		self.tasklist_=tasklist_
		root.bind("<Button-3>", self.showMenu)
		self.window(root)

	def window(self, root):

		left_frame = Frame(root, bg='yellow', width=500)
		left_frame.pack(side=LEFT, fill=Y)

		search_frame = Frame(left_frame, bg=None, height=200, width=500)
		search_frame.pack(side=TOP, fill=X)

		search_label = Label(search_frame, text="资源名称:", bg=None, fg="black", font=("黑体", 12), width=8, height=2,
		                     wraplength=1000,
		                     justify="left", anchor="center")
		search_label.place(x=40, y=80)

		search_keyword = self.search_keyword = Variable()
		search_input = Entry(search_frame, textvariable=search_keyword, width=35)
		search_input.place(x=120, y=87)

		search_button = Button(search_frame, text="搜索", command=self.search_source)
		search_button.place(x=400, y=85)

		# search_label.grid(column=1, row=1)
		# search_input.grid(column=2, row=1)
		# search_button.grid(column=3, padx=20, row=1)

		right_frame = Frame(root, bg='yellow')
		right_frame.pack(side=RIGHT, fill=BOTH, expand=True)

		login_frame = LabelFrame(right_frame, bg=None, height=200, text="登录", font=('黑体', 15))
		login_frame.pack(side=TOP, fill=X, expand=True, anchor='n')

		login_top_blank_frame = Frame(login_frame, bg=None, height=100, width=20, bd=3)
		login_top_blank_frame.pack(side=TOP, fill=X)

		login_name_frame = Frame(login_frame, bg=None, height=60, width=20)
		login_name_frame.pack(side=TOP, fill=X)

		login_password_frame = Frame(login_frame, bg=None, height=60, width=20)
		login_password_frame.pack(side=TOP, fill=X, pady=5)

		login_button_frame = Frame(login_frame, bg=None, height=60, width=20)
		login_button_frame.pack(side=TOP, fill=X, pady=10)

		login_bottom_blank_frame = Frame(login_frame, bg=None, height=100, width=20)
		login_bottom_blank_frame.pack(side=TOP, fill=X)

		# 用户名
		login_name_label = Label(login_name_frame, text="用户名:", bg=None, fg="black", font=("黑体", 8), width=7, height=2,
		                         wraplength=1000,
		                         justify="left", anchor="w")
		login_name_label.pack(side=LEFT, fill=Y, expand=True, anchor='e')

		login_name = self.login_name = Variable()
		login_name_input = Entry(login_name_frame, textvariable=login_name, width=20)
		login_name_input.pack(side=LEFT, fill=Y, expand=True)

		# 密码
		login_password_label = Label(login_password_frame, text="密码:", bg=None, fg="black", font=("黑体", 8), width=7,
		                             height=2,
		                             wraplength=1000,
		                             justify="left", anchor="w")
		login_password_label.pack(side=LEFT, fill=Y, expand=True, anchor='e')

		login_password = self.login_password = Variable()
		login_password_input = Entry(login_password_frame, textvariable=login_password, width=20, show="*")
		login_password_input.pack(side=LEFT, fill=Y, expand=True)

		login_button = Button(login_button_frame, text="登录", command=self.login)
		login_button.pack(side=LEFT, fill=Y, expand=True, anchor='e', padx=10)

		logout_button = Button(login_button_frame, text="注销")
		logout_button.pack(side=LEFT, fill=Y, expand=True, anchor='w', padx=10)

		user_info_frame = LabelFrame(right_frame, bg=None, text="个人信息", font=('黑体', 15))
		user_info_frame.pack(side=TOP, fill=BOTH, expand=True, anchor='n')

		# user_info_sub_frame = Frame(user_info_frame, bg=None, height=300, width=280)
		# user_info_sub_frame.pack(side=TOP, fill=X, expand=True, anchor='n', ipadx=50)
		#
		# user_info_sub_top_blank_frame = Frame(user_info_sub_frame, bg=None, height=40, width=20)
		# user_info_sub_top_blank_frame.pack(side=TOP, fill=X)

		user_info_avatar_frame = Frame(user_info_frame, bg='green', height=50)
		user_info_avatar_frame.pack(side=TOP, fill=BOTH, expand=True, anchor='n')

		user_info_username_frame = Frame(user_info_frame, bg='gray', height=40)
		user_info_username_frame.pack(side=TOP, fill=BOTH, expand=True, anchor='n')

		user_info_telephone_frame = Frame(user_info_frame, bg='blue', height=40)
		user_info_telephone_frame.pack(side=TOP, fill=BOTH, expand=True, anchor='n')

		user_info_is_vip_frame = Frame(user_info_frame, height=40)
		user_info_is_vip_frame.pack(side=TOP, fill=BOTH, expand=True, anchor='n')

		avatar = PhotoImage(file=r'avatar.ppm')
		user_info_avatar = self.avatar = Label(user_info_avatar_frame,
		                                       image=avatar,
		                                       anchor='center', height=50)
		user_info_avatar.image = avatar
		user_info_avatar.pack(side=LEFT, expand=True, fill=BOTH)

		user_info_username_label = Label(user_info_username_frame, text='用户名:  ', height=2, anchor='e', width=15)
		user_info_username_label.pack(side=LEFT, fill=BOTH)

		user_info_username = self.username = Label(user_info_username_frame, height=2, anchor='w')
		user_info_username.pack(side=LEFT, expand=True, fill=BOTH)

		user_info_telephone_label = Label(user_info_telephone_frame, text='手机号:  ', height=2, width=15,
		                                  anchor='e')
		user_info_telephone_label.pack(side=LEFT, fill=BOTH)

		user_info_telephone = self.telephone = Label(user_info_telephone_frame, height=2,
		                                             anchor='w')
		user_info_telephone.pack(side=LEFT, expand=True, fill=BOTH)

		user_info_is_vip_label = Label(user_info_is_vip_frame, text='VIP:      ', height=2, width=15,
		                               anchor='e')
		user_info_is_vip_label.pack(side=LEFT, fill=BOTH)

		user_info_is_vip = self.vip = Label(user_info_is_vip_frame, height=2,
		                                    anchor='w')
		user_info_is_vip.pack(side=LEFT, expand=True, fill=BOTH)

		user_info_sub_bottom_blank_frame = Frame(user_info_frame, bg=None, height=80, width=20)
		user_info_sub_bottom_blank_frame.pack(side=TOP, fill=BOTH)

		table_frame = Frame(left_frame, bg=None, height=400, width=500)
		table_frame.pack(side=TOP, expand=True, fill=BOTH)

		table_tk = self.table_tk = My_Tk(table_frame, user_info=self.user, cookies=base_cookies, headers=base_headers,tasklist_=self.tasklist_)
		resources_list = self.resources_list = table_tk.get_tv()

	# # 表格
	# resources_list = self.resources_list = ttk.Treeview(table_frame, show="headings", padding=LEFT)
	# resources_list.pack(fill=BOTH, expand=True, side=TOP, pady=30)
	#
	# # 定义列
	# resources_list["columns"] = ("no", "name", "author")
	# # 设置列，列还不显示
	# resources_list.column("no", width=30, anchor='w')
	# resources_list.column("name", width=170, anchor='w')
	# resources_list.column("author", width=100, anchor='w')
	#
	# # 设置表头
	# resources_list.heading("no", text="序号")
	# resources_list.heading("name", text="名称")
	# resources_list.heading("author", text="作者")

	# self.root.mainloop()

	def login(self):
		login_url = self.api_uri + "/login"
		login_url_params = {
			'mobile': self.login_name.get(),
			'password': self.login_password.get(),
			'source': 1
		}
		login_headers = base_headers
		login_headers['Host'] = 'api.dushu.io'

		try:
			response = requests.post(url=login_url, json=login_url_params, headers=login_headers)
			data = response.json()
		except BaseException:
			messagebox.showerror("提示", message="登录失败")
			return
		else:
			if data['status'] == 1:
				self.rebind_user_info(data=data)
				base_cookies["SERVERID"] = response.cookies.get("SERVERID")
				print(response.cookies)
				self.user['token'] = data['token']

	# messagebox.askyesno("确认吗？", message=json)

	def logout(self):
		pass

	def showMenu(self, event):
		pass

	# self.menubar.post(event.x_root, event.y_root)

	def search_source(self):
		try:
			keyword = self.search_keyword.get()
			search_params = {"appId": 2002, 'keyword': keyword}
			if 'token' in self.user:
				search_params['token'] = self.user['token']
			search_headers = base_headers
			search_headers['Host'] = 'gateway-api.dushu.io'
			search_url = self.gateway_url + "/search-orchestration-system/search/v100/searchUnited"
			response = requests.post(url=search_url, json=search_params, headers=search_headers, cookies=base_cookies)
			search_result = response.json()
		except BaseException:
			messagebox.showerror("错误", message="搜索异常")
		else:
			if search_result['status'] == '0000':
				self.load_data(search_result['data'])

	def load_data(self, data):
		# 加载前先清空
		[self.resources_list.delete(node) for node in self.resources_list.get_children()]
		print(data)
		index = 0
		rows = []
		for resource in data['bookRes']['list']:
			fragementId = resource['fragementId']
			item = (index + 1, resource['title'], resource['author'], fragementId)
			rows.append(item)
			index = index + 1
		self.table_tk.insert_tv(rows)

	def download(self):
		pass

	def run(self):
		pass

	def rebind_user_info(self, data=None):
		if data == None:
			return
		avatar = self.tranform_image(data['avatarUrl'])
		self.avatar.config(image=avatar)
		self.avatar.image = avatar
		self.username.config(text=data['username'])
		self.telephone.config(text=data['mobile'])
		self.vip.config(text='是' if data['is_vip'] else '否')

	def tranform_image(self, url):
		# try:
		if(url.startswith('https')):
			url='http'+url[5:]
		response = requests.get(
			url=url)
		# except BaseException:
		# 	print("图片下载失败")
		# else:
		image = Image.open(BytesIO(response.content))
		image = image.resize((40, 40), Image.ANTIALIAS)
		image.save(r"images\avatar.ppm")
		return PhotoImage(file=r'images\avatar.ppm')


# table_frame = Frame(win, bg="blue")
# table_frame.pack(side=BOTTOM, expand=True, fill=BOTH)


if __name__ == '__main__':
	win = Tk()
	win.title("视频下载器")
	win.geometry("800x600+400+250")
	win.iconbitmap(bitmap=None)
	# win.maxsize(width=800,height=600)
	win.resizable(width=False, height=False)
	app = application(win)
	win.mainloop()
