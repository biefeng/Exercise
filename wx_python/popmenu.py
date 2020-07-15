# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/07/15 13:53
# file_name : popmenu.py

# coding=utf-8
import wx


class MyFrame2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        self.m_menu6 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem(self.m_menu6, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu6.Append(self.m_menuItem1)

        self.m_menuItem2 = wx.MenuItem(self.m_menu6, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu6.Append(self.m_menuItem2)

        self.m_menuItem3 = wx.MenuItem(self.m_menu6, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu6.Append(self.m_menuItem3)

        button = wx.Button(self, label="12")

        self.Bind(wx.EVT_CONTEXT_MENU, self.MyFrame2OnContextMenu)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

    def MyFrame2OnContextMenu(self, event):
        # self.PopupMenu(self.m_menu6, event.GetPosition())
        self.PopupMenu(self.m_menu6, wx.DefaultPosition)


app = wx.App(False)
frame = MyFrame2(None)
frame.Show(True)
# start the applications
app.MainLoop()
