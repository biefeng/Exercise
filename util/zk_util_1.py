# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/07/10 17:23
# file_name : zk_util_1.py

import wx
from kazoo.client import KazooClient
from kazoo.recipe.cache import TreeCache
import threading


class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title="vbox", size=(1700, 900))  # 继承wx.Frame类

        self._zk_client = KazooClient("localhost:2181")
        # self._zk_client = KazooClient(hosts='10.128.62.34:2181,10.128.62.34:2182,10.128.62.34:2183')
        self._zk_client.start()
        cached_tree = self.cached_tree = TreeCache(self._zk_client, "/")
        cached_tree.start()
        self.Center()
        splitter = wx.SplitterWindow(self, -1)
        leftpanel = wx.Panel(splitter)
        rigntpanel = wx.Panel(splitter)
        splitter.SplitVertically(leftpanel, rigntpanel, 500)
        splitter.SetMinimumPaneSize(80)

        self.tree = self.CreateTreeCtrl(leftpanel)

        # self.Bind(wx.EVT_TREE_SEL_CHANGING, self.on_listbox, self.tree)

        vbox1 = wx.BoxSizer(wx.VERTICAL)
        node_filter = wx.TextCtrl(leftpanel)

        vbox1.Add(node_filter, 1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox1.Add(self.tree, 1, flag=wx.ALL | wx.EXPAND, border=5)
        leftpanel.SetSizer(vbox1)

        vbox2 = wx.BoxSizer(wx.VERTICAL)
        self.content = wx.StaticText(rigntpanel, label='右侧面板')

        vbox2.Add(self.content, 1, flag=wx.ALL | wx.EXPAND, border=5)
        rigntpanel.SetSizer(vbox2)

    def on_listbox(self, item, path=None):
        if path is None:
            path = self.get_current_path(item)
        data, state = self._zk_client.get(path)
        self.content.SetLabel(self.tree.GetItemText(item))

    def CreateTreeCtrl(self, parent):
        tree = wx.TreeCtrl(parent)
        imglist = wx.ImageList(16, 16, True, 3)

        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, size=wx.Size(16, 16)))
        # imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, size=wx.Size(16, 16)))
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, size=wx.Size(16, 16)))

        tree.AssignImageList(imglist)
        tree.Bind(wx.EVT_TREE_SEL_CHANGING, self.on_open)
        tree.Bind(wx.EVT_TREE_ITEM_EXPANDING, self.on_open)
        items = []
        root = self.root = tree.AddRoot('/', image=0)
        # self.init_tree(tree, root)

        self.treeify_recursive("/", root, tree)

        return tree

    def init_tree(self, tree, root):
        client = self._zk_client
        self.open_path("/", tree, root)

    def open_path(self, path, tree, root):

        # def inner():
        client = self._zk_client
        # tree.DeleteChildren(root)
        children = client.get_children(path)
        for child in children:
            top_path = path + child + "/"
            sub_childern = client.get_children(top_path)
            cl = len(sub_childern)
            item = tree.AppendItem(root, child, (0 if cl > 0 else 1))
            # tree.AppendItem(root, child, 1)
            for sub_child in sub_childern:
                scl = len(client.get_children(top_path + "/" + sub_child))
                tree.AppendItem(item, sub_child, (0 if scl > 0 else 1))

    # thread = threading.Thread(target=inner)
    # thread.start()

    def on_open(self, event):
        item = event.Item
        if item.ID is None:
            return
        path = self.get_current_path(item)
        print(path)
        # self.open_path(path, self.tree, item)
        self.on_listbox(item, path)

    def get_current_path(self, item):
        tree = self.tree
        current_item_text = tree.GetItemText(item)
        pid = tree.GetItemParent(item)
        if pid.ID is None:
            return '/'
        else:
            return self.get_current_path(pid) + current_item_text + "/"

    def treeify_recursive(self, path, parent, tree):
        cached_tree = self.cached_tree
        client = self._zk_client
        cd = cached_tree.get_children(path=path)
        if cd is None or len(cd) == 0:
            cd = client.get_children(path)
        if cd and len(cd) > 0:
            for i, c in enumerate(cd):
                tmp_path = path + c + '/'
                tc = cached_tree.get_children(tmp_path)
                if tc is None or len(tc) == 0:
                    tc = client.get_children(tmp_path)
                if tc and len(tc) > 0:
                    insert = tree.AppendItem(parent, c, 0)
                    self.treeify_recursive(path=tmp_path, parent=insert, tree=tree)
                else:
                    tree.AppendItem(parent, c, 1)

    def clear_cached_tree(self):
        self.cached_tree.close()


class App(wx.App):
    def OnInit(self):  # 进入
        self.frame = frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):  # 退出
        self.frame.clear_cached_tree()
        print("tuichu")
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()
