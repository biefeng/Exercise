# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/07/10 9:25
# file_name : zk_util.py


import logging

import tkinter as tk
from tkinter.ttk import Treeview, Scrollbar

from kazoo.client import KazooClient

logging.basicConfig()


class NodeTree:
    def __init__(self):
        self._client = KazooClient(hosts='localhost:2181')
        # self._client = KazooClient(hosts='10.128.62.34:2181,10.128.62.34:2182,10.128.62.34:2183')
        self._client.start()
        self._selected_node = None
        self._win = None
        self._root = None
        self._tree_canvas = None
        self._tree_frame_id = None
        self.init_ui()
        self.init_tree()
        self._count = 0
        # self.treeify()

        print(self._count)
        self._win.mainloop()

    def init_ui(self):
        self._win = tk.Tk()
        self._win.title("zk-client")
        self._win.geometry('900x700+500+300')
        self._win.resizable(height=False, width=False)
        tree_wrapper = tk.Frame(self._win, bg='red', width=300)
        tree_wrapper.pack(side=tk.LEFT, fill=tk.Y)

        canvas = self._tree_canvas = tk.Canvas(tree_wrapper, width=300, height=700, scrollregion=(0, 0, 300, 700), bg='gray')  # 创建canvas
        canvas.place(x=0, y=0)  # 放置canvas的位置

        frame = tk.Frame(canvas)  # 把frame放在canvas里
        # frame.place(width=180, height=600)  # frame的长宽，和canvas差不多的
        vbar = Scrollbar(canvas, orient=tk.VERTICAL)  # 竖直滚动条
        vbar.place(x=281, width=20, height=700)
        vbar.configure(command=canvas.yview)
        hbar = Scrollbar(canvas, orient=tk.HORIZONTAL)  # 水平滚动条
        hbar.place(x=0, y=680, width=280, height=20)
        hbar.configure(command=canvas.xview)
        canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)  # 设置
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

        self._tree_frame_id = canvas.create_window(0, 0, window=frame, anchor='nw')  # create_window)

        self._root = Treeview(frame)
        #
        self._root.pack(expand=True, fill=tk.BOTH)
        # self._root.bind("<Button-1>", self.clear_pre_selected)
        # self._root.bind("<< TreeviewClose>>", self.clear_pre_selected)
        self._root.bind("<<TreeviewOpen>>", self.open_node)

    def adjust_size(self):
        self._root.update()
        width = self._root.winfo_width()
        height = self._root.winfo_height()
        print(width,height)
        self._tree_canvas.itemconfigure(self._tree_frame_id, height=height)  # 设定窗口tv_frame的高度
        self._tree_canvas.config(scrollregion=(0, 0, width, height))
        self._tree_canvas.config(scrollregion=self._tree_canvas.bbox("all"))  # 滚动指定的范围
        self._tree_canvas.config(height=height)
        pass

    def init_tree(self):
        tops = self._client.get_children("/")
        for index, top in enumerate(tops):
            self._root.insert('', index, text=top)
            children = self._client.get_children("/" + top + "/")
            if children is not None and len(children) > 0:
                pass

    def clear_pre_selected(self, event):
        focus = self._root.focus()
        if focus == '':
            return
        children = self._root.get_children(focus)
        for child in children:
            self._root.delete(child)

    def open_node(self, event):
        iid = self._root.focus()
        path = self.get_current_path(iid)
        children = self._client.get_children(path)
        for index, p in enumerate(children):
            self._root.insert(iid, index, text=p)
        self.adjust_size()

    def get_current_path(self, item):
        curr_item = self._root.item(item)
        pid = self._root.parent(item)
        if pid == '':
            return '/' + curr_item['text'] + "/"
        else:
            return self.get_current_path(pid) + curr_item['text'] + "/"

    def treeify(self):
        self._client.start()
        self.treeify_recursive("/", parent='', index=0)

    def treeify_recursive(self, path, parent, index):
        self._count += 1
        cd = self._client.get_children(path=path)
        if cd and len(cd) > 0:
            for i, c in enumerate(cd):
                tmp_path = path + c + '/'
                tc = self._client.get_children(tmp_path)
                if tc and len(tc) > 0:
                    insert = self._root.insert(parent, i, text=c)
                    self.treeify_recursive(path=tmp_path, parent=insert, index=i)
                else:
                    self._root.insert(parent, i, text=c)


if __name__ == '__main__':
    tree = NodeTree()
    # tk = Tk()
    # widget = Widget(tk, "1")
    # widget.pack(fill=X)
    # tk.mainloop()
