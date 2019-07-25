# -*- coding: utf-8 -*-
__author__ = '33504'

from tkinter import *
from tkinter import filedialog, messagebox


class tasklist:

    def __init__(self):
        self.index = 1
        self.rows = {}

    def test(self):
        lineheight = 25
        height = lineheight * 21
        self.canvas.itemconfigure(self.canvas_create_window, height=height)
        print(self.canvas.bbox('all'))
        self.canvas.config(scrollregion=self.canvas.bbox('all'))
        self.tv.update()
        print(self.canvas)
        for i in range(20):
            self.insert_data(("1", "第三选择", self.catch_progress_bar()))
            print("index: " + str(i))
        print("finished")

    def catch_progress_bar(self):
        progress_bar = Frame(self.progress_bar_frame)
        progress_bar.pack(side=TOP)
        canvas = Canvas(progress_bar, width=235, height=19, bg='grey')
        canvas.pack(side=TOP)
        return canvas

    def insert_data(self, row):
        self.rows[row[0]] = row
        index = Label(self.index_frame, text=self.index, height=1, bg='orange')
        index.pack(side=TOP, pady=0.5, fill=X)

        name = Label(self.name_frame, anchor='w', text=row[1], bg="orange")
        name.pack(side=TOP, pady=0.5, fill=X)

        name = Label(self.download_time_frame, text=row[2], bg="orange")
        name.pack(side=TOP, pady=0.5, fill=X)

        self.progress_bar = Frame(self.progress_bar_frame, bg="orange")
        self.progress_bar.pack(side=TOP, pady=0.5, fill=X)

        # canvas = Canvas(self.progress_bar, width=235, height=19, bg='white')
        # canvas.pack(side=TOP, expand=True, fill=BOTH)

        self.index = self.index + 1

    # x = 300
    # n = 220 / x
    # for i in range(x):
    # 	n = n + (220 / x)
    # 	self.progress(canvas, n)

    def progress(self, bar, n):
        fill_line = bar.create_rectangle(10, 10, 2, 10, width=0, fill='green')
        bar.coords(fill_line, (0, 0, n, 60))
        self.tv.update()

    def set_download_dir(self):
        selected_dir = filedialog.askdirectory()
        if selected_dir:
            self.download_dir.set(selected_dir)
            self.tv.update()
            print(selected_dir)

    def create_tasklist_tv(self, tv):

        download_dir_label = Label(tv, text="下载路径: ", font=("黑体", 12), bg="white")
        download_dir_label.place(x=25, y=20)

        self.download_dir = StringVar(value=r"d:\\")
        self.download_dir_entry = Entry(tv, bd=2, textvariable=self.download_dir, state="readonly")
        self.download_dir_entry.place(x=115, y=21, width=500, height=23)

        select_dir_button = Button(tv, text="选择文件夹", command=self.set_download_dir)
        select_dir_button.place(x=620, y=18)

        Label(tv, text="下载类型: ", font=("黑体", 12), bg="white").place(x=25, y=50)

        self.media_type_var = Variable(value=".mp3")
        Radiobutton(tv, text="MP3", bg="white", variable=self.media_type_var, value=".mp3").place(x=110, y=50)
        Radiobutton(tv, text="MP4", bg="white", variable=self.media_type_var, value=".mp4").place(x=170, y=50)
        self.tv = tv
        header_frame = Frame(tv, bg="white")
        header_frame.place(relx=0.032, rely=0.37, relwidth=0.906, height=20)

        progress_bar_head = Label(header_frame, text="序号", bg="white", bd=2, relief=RIDGE, anchor="center")
        # progress_bar_head.pack(side=LEFT, fill=BOTH)
        progress_bar_head.place(relx=0.002, rely=0.005, relwidth=0.06, relheight=0.99)

        progress_bar_head = Label(header_frame, text="名称", bg="white", bd=2, relief=RIDGE, anchor="center")
        progress_bar_head.place(relx=0.061, rely=0.005, relwidth=0.455, relheight=0.99)

        progress_bar_head = Label(header_frame, text="下载时间", bg="white", bd=2, relief=RIDGE, anchor="center")
        progress_bar_head.place(relx=0.515, rely=0.005, relwidth=0.191, relheight=0.99)
        #
        progress_bar_head = Label(header_frame, text="进度", bg="white", bd=2, relief=RIDGE, anchor="center")
        progress_bar_head.place(relx=0.701, rely=0.005, relwidth=0.28, relheight=0.99)

        canvas = self.canvas = Canvas(tv, width=760, height=300, scrollregion=(0, 0, 800, 300), bg="white",
                                      bd=0)  # 创建canvas
        canvas.place(x=10, y=250)  # 放置canvas的位置
        frame = Frame(canvas, bg="white", bd=0)  # 把frame放在canvas里
        frame.place(x=0, y=0, width=760, height=300)  # frame的长宽，和canvas差不多的

        vbar = Scrollbar(canvas, orient=VERTICAL)  # 竖直滚动条
        vbar.place(x=751, y=0, width=10, height=300)
        vbar.configure(command=canvas.yview)

        canvas.config(yscrollcommand=vbar.set)  # 设置
        self.canvas_create_window = canvas.create_window(0, 0, window=frame, anchor="nw", width=760, height=300)

        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

        # *****************************

        self.index_frame = Frame(frame, bd=2, relief=RIDGE, bg="white")
        self.index_frame.place(relx=0.022, rely=0.005, relwidth=0.061, relheight=0.99)

        self.name_frame = Frame(frame, bd=2, relief=RIDGE, bg="white")
        self.name_frame.place(relx=0.079, rely=0.005, relwidth=0.458, relheight=0.99)

        self.download_time_frame = Frame(frame, bd=2, relief=RIDGE, bg="white")
        self.download_time_frame.place(relx=0.518, rely=0.005, relwidth=0.188, relheight=0.99)

        self.progress_bar_frame = Frame(frame, bd=2, relief=RIDGE, bg="white")
        self.progress_bar_frame.place(relx=0.7, rely=0.005, relwidth=0.27, relheight=0.99)


if __name__ == '__main__':
    win = Tk()

    win.geometry("800x600+200+50")
    win.title("任务列表")
    t = tasklist()
    t.create_tasklist_tv(win)

    win.mainloop()
