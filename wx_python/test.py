# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class MyFrame1
###########################################################################
from kazoo.client import KazooClient


class MyProgressBarDialog(wx.Dialog):

    def __init__(self):
        wx.Dialog.__init__(self, None, -1)

        ag_fname = "C:\\bob2.gif"

        ag = wx.AnimationCtrl(self, -1, ag_fname)

        ag.GetPlayer().UseBackgroundColour(True)

        ag.Play()


class MyFrame1(wx.Frame):
    def search(self, evt):
        value = self.m_textCtrl8.GetValue()
        self.treeify_recursive("/", self.root_node, self.m_treeCtrl7)

    def treeify_recursive(self, path, parent, tree):
        client = self._zk_client
        cd = client.get_children(path=path)
        if cd and len(cd) > 0:
            for i, c in enumerate(cd):
                tmp_path = path + c + '/'
                tc = client.get_children(tmp_path)
                if tc and len(tc) > 0:
                    insert = tree.AppendItem(parent, c, 0)
                    self.treeify_recursive(path=tmp_path, parent=insert, tree=tree)
                else:
                    tree.AppendItem(parent, c, 1)

    def __init__(self, parent):

        self._zk_client = KazooClient("localhost:2181")
        self._zk_client.start()
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(1029, 722), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

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
        bSizer17.Add(self.m_textCtrl8, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_button3 = wx.Button(self.m_panel7, wx.ID_ANY, u"search", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button3.Bind(wx.EVT_BUTTON, self.search)
        bSizer17.Add(self.m_button3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_panel7.SetSizer(bSizer17)
        self.m_panel7.Layout()
        bSizer17.Fit(self.m_panel7)
        self.m_panel8 = wx.Panel(self.m_splitter9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel8.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer20 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_treeCtrl7 = wx.TreeCtrl(self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer20.Add(self.m_treeCtrl7, 1, wx.ALL | wx.EXPAND, 5)

        self.root_node = self.m_treeCtrl7.AddRoot("/")

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

        self.m_button5 = wx.Button(self.m_panel11, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer21.Add(self.m_button5, 0, wx.ALL, 5)

        self.m_textCtrl10 = wx.TextCtrl(self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_WORDWRAP)
        self.m_textCtrl10.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer21.Add(self.m_textCtrl10, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel11.SetSizer(bSizer21)
        self.m_panel11.Layout()
        bSizer21.Fit(self.m_panel11)
        self.m_notebook1.AddPage(self.m_panel11, u"Node data", False)
        self.m_panel12 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl(self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_dataViewListColumn1 = self.m_dataViewListCtrl1.AppendTextColumn(u"Name")
        self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.AppendTextColumn(u"Value")
        bSizer8.Add(self.m_dataViewListCtrl1, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel12.SetSizer(bSizer8)
        self.m_panel12.Layout()
        bSizer8.Fit(self.m_panel12)
        self.m_notebook1.AddPage(self.m_panel12, u"Node Metadata", True)
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
        self.Connect = wx.Menu()
        self.m_menubar1.Append(self.Connect, u"Connect")

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


app = wx.App(False)
frame = MyFrame1(None)
frame.Show(True)
# start the applications
app.MainLoop()
