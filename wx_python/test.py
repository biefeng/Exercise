# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import os
import sys
from concurrent.futures.thread import ThreadPoolExecutor

import wx
import wx.adv
import wx.dataview
import wx.xrc
###########################################################################
## Class MyFrame1
###########################################################################
from kazoo.client import KazooClient


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class MyDialog1(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(399, 120), style=wx.DEFAULT_DIALOG_STYLE)
        self.main = parent
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.m_splitter3 = wx.SplitterWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D)
        self.m_splitter3.Bind(wx.EVT_IDLE, self.m_splitter3OnIdle)

        self.m_panel10 = wx.Panel(self.m_splitter3, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.TAB_TRAVERSAL)
        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(self.m_panel10, wx.ID_ANY, u"URL", wx.DefaultPosition, wx.Size(50, -1), 0)
        self.m_staticText2.Wrap(-1)
        bSizer13.Add(self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_textCtrl13 = wx.TextCtrl(self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, 30), 0)
        self.m_textCtrl13.SetValue("localhost:2181")
        bSizer13.Add(self.m_textCtrl13, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_panel10.SetSizer(bSizer13)
        self.m_panel10.Layout()
        bSizer13.Fit(self.m_panel10)
        self.m_panel11 = wx.Panel(self.m_splitter3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer15 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText5 = wx.StaticText(self.m_panel11, wx.ID_ANY, u"Timeout", wx.DefaultPosition, wx.Size(50, -1), 0)
        self.m_staticText5.Wrap(-1)
        bSizer11.Add(self.m_staticText5, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_textCtrl14 = wx.TextCtrl(self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, 30), 0)
        self.m_textCtrl14.SetValue('10')
        bSizer11.Add(self.m_textCtrl14, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer15.Add(bSizer11, 1, wx.EXPAND, 5)

        self.m_button3 = wx.Button(self.m_panel11, wx.ID_ANY, u"Connect", wx.Point(-1, -1), wx.DefaultSize, 0)
        self.m_button3.Bind(wx.EVT_BUTTON, self.connect)
        bSizer15.Add(self.m_button3, 0, wx.ALL, 5)

        self.m_panel11.SetSizer(bSizer15)
        self.m_panel11.Layout()
        bSizer15.Fit(self.m_panel11)
        self.m_splitter3.SplitHorizontally(self.m_panel10, self.m_panel11, 0)
        bSizer9.Add(self.m_splitter3, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer9)
        self.Layout()

        self.Centre(wx.BOTH)

    def connect(self, evt):
        main = self.main
        url = self.m_textCtrl13.GetValue()
        timeout = self.m_textCtrl14.GetValue()
        try:
            timeout = int(timeout)
        except Exception as e:
            timeout = 10
            print(e)
        try:
            main.zk_connect(url, timeout)
        except Exception as e:
            main.messageDialog.SetMessage("Connect Error")
            main.messageDialog.Show()
        self.Close()

    def __del__(self):
        pass

    def m_splitter3OnIdle(self, event):
        self.m_splitter3.SetSashPosition(0)
        self.m_splitter3.Unbind(wx.EVT_IDLE)


class MyFrame1(wx.Frame):
    def search(self, evt):
        value = self.m_textCtrl8.GetValue()
        tree = self.m_treeCtrl7 
        selection = tree.GetSelection()
        if selection is None:
            return
        self.recursive_search(selection, value)

    def recursive_search(self, item, text):

        tree = self.m_treeCtrl7
        (child, cookie) = tree.GetFirstChild(item)
        while child.IsOk():
            item_text = tree.GetItemText(child)
            print(tree.GetItemText(child))
            self.recursive_search(child, text)
            if item_text.find(text) >= 0:
                tree.SelectItem(child)
                tree.Expand(item)
                print("---------")
            (child, cookie) = tree.GetNextChild(child, cookie)

    def load(self, evt):

        if self._zk_client is None:
            self.messageDialog.SetMessage("please click the connect button and connect to zookeeper server.")
            self.messageDialog.ShowModal()
            return

        self.loading()
        self.m_treeCtrl7.DeleteChildren(self.root_node)
        # thread = threading.Thread(target=self.do_search)
        # thread.start()
        self.thread_pool_executor.submit(self.do_load)

    def do_load(self):
        self.treeify_recursive("/", self.root_node, self.m_treeCtrl7)
        self.close_loading()

    def loading(self):
        self.animation_ctrl.SetAnimation(self.loading_animation)
        self.animation_ctrl.Play()

    def close_loading(self):
        self.animation_ctrl.SetAnimation(wx.adv.NullAnimation)
        self.animation_ctrl.Stop()
        self.m_treeCtrl7.Expand(self.root_node)

    def treeify_recursive(self, path, parent, tree):

        client = self._zk_client
        cd = client.get_children(path=path)

        if cd and len(cd) > 0:
            cd.sort()
            for i, c in enumerate(cd):
                tmp_path = path + c + '/'
                tc = client.get_children(tmp_path)
                if tc and len(tc) > 0:
                    insert = tree.AppendItem(parent, c, 0)
                    self.treeify_recursive(path=tmp_path, parent=insert, tree=tree)
                else:
                    tree.AppendItem(parent, c, 1)

    def open_dialog(self, evt):
        dialog_ = MyDialog1(self)
        dialog_.Show()

    def load_data(self, event):
        item = event.GetItem()
        path = self.get_current_path(item)
        client = self._zk_client
        if client is None:
            return
        data, state = client.get(path)
        print(data)
        if data is not None:
            self.m_textCtrl10.SetValue(data)
        else:
            self.m_textCtrl10.SetValue("")
        self.m_dataViewListCtrl1.DeleteAllItems()
        for field in state._fields:
            value = getattr(state, field)
            self.m_dataViewListCtrl1.AppendItem([field, str(value)])
        acls, id = client.get_acls(path)

    def zk_connect(self, url, timeout=10):
        self._zk_client = KazooClient(hosts=url, timeout=timeout)
        self._zk_client.start()

    def get_current_path(self, item):
        tree = self.m_treeCtrl7
        current_item_text = tree.GetItemText(item)
        pid = tree.GetItemParent(item)
        if pid.ID is None:
            return '/'
        else:
            return self.get_current_path(pid) + current_item_text + "/"

    def copy_path(self, item):
        path = self.get_current_path(item)

        text_obj = wx.TextDataObject()
        text_obj.SetText(path)
        if wx.TheClipboard.IsOpened() or wx.TheClipboard.Open():
            wx.TheClipboard.SetData(text_obj)
            wx.TheClipboard.Close()

    def copy_name(self, item):
        name = self.m_treeCtrl7.GetItemText(item)
        # name = urllib.parse.unquote(name)
        text_obj = wx.TextDataObject()
        text_obj.SetText(name)
        if wx.TheClipboard.IsOpened() or wx.TheClipboard.Open():
            wx.TheClipboard.SetData(text_obj)
            wx.TheClipboard.Close()

    def delete_node(self, item):
        self.loading()
        self.thread_pool_executor.submit(self.do_delete_node, item)

    def do_delete_node(self, item):
        client = self._zk_client

        path = self.get_current_path(item)
        parent = self.m_treeCtrl7.GetItemParent(item)
        if client:
            self.m_treeCtrl7.Collapse(parent)
            client.delete(path, recursive=True)

        parent_id = parent.ID
        if parent_id is None:
            self.load(None)
        else:
            parent_path = self.get_current_path(parent)
            self.m_treeCtrl7.DeleteChildren(parent)
            self.treeify_recursive(parent_path, parent, self.m_treeCtrl7)
            self.m_treeCtrl7.Expand(parent)

        self.close_loading()

    def refresh_node(self, item):
        self.loading()
        self.thread_pool_executor.submit(self.do_refresh_node, item)

    def do_refresh_node(self, item):
        path = self.get_current_path(item)
        self.m_treeCtrl7.Collapse(item)
        self.m_treeCtrl7.DeleteChildren(item)
        self.treeify_recursive(path, item, self.m_treeCtrl7)
        self.close_loading()

    def copy_value(self, evt):
        item = evt.GetItem()
        row = self.m_dataViewListCtrl1.ItemToRow(item)
        value = self.m_dataViewListCtrl1.GetValue(row, 1)

        selected = self.m_dataViewListCtrl1.GetPopupMenuSelectionFromUser(self.m_menu22, wx.DefaultPosition)
        if selected is None:
            return
        selected_item = self.m_menu22.FindItemById(selected)
        if selected_item is None:
            return
        text_obj = wx.TextDataObject()
        text_obj.SetText(value)
        if wx.TheClipboard.IsOpened() or wx.TheClipboard.Open():
            wx.TheClipboard.SetData(text_obj)
            wx.TheClipboard.Close()

    def TreeCtlOnContextMenu(self, event):
        tree_item = event.GetItem()
        selected = self.GetPopupMenuSelectionFromUser(self.m_menu21, wx.DefaultPosition)
        if selected is None:
            return
        selected_item = self.m_menu21.FindItemById(selected)
        if selected_item is None:
            return
        selected_item.handler(tree_item)

    def __init__(self, parent):
        self.thread_pool_executor = ThreadPoolExecutor(max_workers=1)
        self._zk_client = None
        # self._zk_client = KazooClient(hosts='10.128.62.34:2181,10.128.62.34:2182,10.128.62.34:2183')

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(1029, 722), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.messageDialog = wx.GenericMessageDialog(self, wx.EmptyString)
        self.messageDialog.SetOKLabel("OK")
        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_splitter2 = wx.SplitterWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D)
        self.m_splitter2.Bind(wx.EVT_IDLE, self.m_splitter2OnIdle)

        self.m_panel3 = wx.Panel(self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.m_splitter9 = wx.SplitterWindow(self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D)
        self.m_splitter9.Bind(wx.EVT_IDLE, self.m_splitter9OnIdle)

        self.m_splitter9.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        self.m_panel7 = wx.Panel(self.m_splitter9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel7.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer17 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl8 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        bSizer17.Add(self.m_textCtrl8, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_button3 = wx.Button(self.m_panel7, wx.ID_ANY, u"search", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button3.Bind(wx.EVT_BUTTON, self.search)
        bSizer17.Add(self.m_button3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_panel7.SetSizer(bSizer17)
        self.m_panel7.Layout()
        bSizer17.Fit(self.m_panel7)
        self.m_panel8 = wx.Panel(self.m_splitter9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel8.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer20 = self.bSizer20 = wx.BoxSizer(wx.VERTICAL)

        self.loading_animation = wx.adv.Animation()
        self.loading_animation.LoadFile(resource_path("loading.gif"))
        self.animation_ctrl = wx.adv.AnimationCtrl(self.m_panel8, wx.ID_ANY, anim=wx.adv.NullAnimation, size=(20, 20), pos=wx.DefaultPosition)
        self.bSizer20.Add(self.animation_ctrl, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_treeCtrl7 = wx.TreeCtrl(self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, style=wx.TR_DEFAULT_STYLE)
        bSizer20.Add(self.m_treeCtrl7, 1, wx.ALL | wx.EXPAND, 5)

        self.root_node = self.m_treeCtrl7.AddRoot("/", 0)

        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, size=wx.Size(16, 16)))
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, size=wx.Size(16, 16)))

        self.m_treeCtrl7.AssignImageList(imglist)

        self.m_treeCtrl7.Bind(wx.EVT_TREE_ITEM_MENU, self.TreeCtlOnContextMenu)
        self.m_treeCtrl7.Bind(wx.EVT_TREE_SEL_CHANGING, self.load_data)

        self.m_menu21 = wx.Menu()
        self.m_menu21_m_menuItem1 = wx.MenuItem(self.m_menu21, wx.ID_ANY, u"copy path", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu21_m_menuItem1.handler = self.copy_path
        self.m_menu21.Append(self.m_menu21_m_menuItem1)

        self.m_menu21_m_menuItem2 = wx.MenuItem(self.m_menu21, wx.ID_ANY, u"copy name", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu21_m_menuItem2.handler = self.copy_name
        self.m_menu21.Append(self.m_menu21_m_menuItem2)

        self.m_menu21_m_menuItem3 = wx.MenuItem(self.m_menu21, wx.ID_ANY, u"delete node", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu21_m_menuItem3.handler = self.delete_node
        self.m_menu21.Append(self.m_menu21_m_menuItem3)

        self.m_menu21_m_menuItem4 = wx.MenuItem(self.m_menu21, wx.ID_ANY, u"refresh", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu21_m_menuItem4.handler = self.refresh_node
        self.m_menu21.Append(self.m_menu21_m_menuItem4)

        self.m_menu22 = wx.Menu()
        self.m_menu22_m_menuItem1 = wx.MenuItem(self.m_menu22, wx.ID_ANY, u"copy value", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu22.Append(self.m_menu22_m_menuItem1)
        # self.m_menu22_m_menuItem1.handler = self.copy_value

        self.m_panel8.SetSizer(bSizer20)
        self.m_panel8.Layout()
        bSizer20.Fit(self.m_panel8)
        self.m_splitter9.SplitHorizontally(self.m_panel7, self.m_panel8, 40)
        bSizer12.Add(self.m_splitter9, 1, wx.EXPAND, 5)

        self.m_panel3.SetSizer(bSizer12)
        self.m_panel3.Layout()
        bSizer12.Fit(self.m_panel3)
        self.m_panel4 = wx.Panel(self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.Size(200, -1), wx.NO_BORDER)
        bSizer19 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook1 = wx.Notebook(self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panel11 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer21 = wx.BoxSizer(wx.VERTICAL)

        self.m_button5 = wx.Button(self.m_panel11, wx.ID_ANY, u"save", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer21.Add(self.m_button5, 0, wx.ALL, 5)

        self.m_textCtrl10 = wx.TextCtrl(self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_WORDWRAP)
        self.m_textCtrl10.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer21.Add(self.m_textCtrl10, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel11.SetSizer(bSizer21)
        self.m_panel11.Layout()
        bSizer21.Fit(self.m_panel11)
        self.m_notebook1.AddPage(self.m_panel11, u"Node data", True)
        self.m_panel12 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl(self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, style=wx.dataview.DV_HORIZ_RULES | wx.dataview.DV_VERT_RULES)
        self.m_dataViewListColumn1 = self.m_dataViewListCtrl1.AppendTextColumn(u"Name", width=350)
        self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.AppendTextColumn(u"Value")

        self.m_dataViewListCtrl1.Bind(wx.dataview.EVT_DATAVIEW_ITEM_CONTEXT_MENU, self.copy_value)

        bSizer8.Add(self.m_dataViewListCtrl1, 1, wx.ALL | wx.EXPAND, 5)
        # self.m_propertyGrid1 = pg.PropertyGrid(self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PG_DEFAULT_STYLE | wx.propgrid.PG_SPLITTER_AUTO_CENTER)
        self.m_panel12.SetSizer(bSizer8)
        self.m_panel12.Layout()
        bSizer8.Fit(self.m_panel12)
        self.m_notebook1.AddPage(self.m_panel12, u"Node Metadata", False)
        self.m_panel13 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_notebook1.AddPage(self.m_panel13, u"Node Acl", False)

        bSizer19.Add(self.m_notebook1, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel4.SetSizer(bSizer19)
        self.m_panel4.Layout()
        self.m_splitter2.SplitVertically(self.m_panel3, self.m_panel4, 300)
        bSizer4.Add(self.m_splitter2, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer4)
        self.Layout()
        self.m_menubar1 = wx.MenuBar(0)
        self.connect_btn = wx.Menu()
        self.m_menubar1.Append(self.connect_btn, u"Connect")
        self.refresh_btn = wx.Menu()
        self.m_menubar1.Append(self.refresh_btn, u"Refresh")
        self.connect_btn.Bind(wx.EVT_MENU_OPEN, self.open_dialog)
        self.refresh_btn.Bind(wx.EVT_MENU_OPEN, self.load)

        self.SetMenuBar(self.m_menubar1)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

    def m_splitter2OnIdle(self, event):
        self.m_splitter2.SetSashPosition(300)
        self.m_splitter2.Unbind(wx.EVT_IDLE)

    def m_splitter9OnIdle(self, event):
        self.m_splitter9.SetSashPosition(40)
        self.m_splitter9.Unbind(wx.EVT_IDLE)


# app = wx.App(False)
# frame = MyFrame1(None)
# frame.Show(True)
# start the applications
# app.MainLoop()


class App(wx.App):
    def OnInit(self):  # 进入
        self.frame = frame = MyFrame1(None)
        frame.Show()
        return True

    def OnExit(self):  # 退出

        print("tuichu")
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()
