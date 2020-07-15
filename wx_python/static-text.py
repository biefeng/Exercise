# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/07/15 18:39
# file_name : static-text.py

# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame3
###########################################################################
from wx.lib.expando import ExpandoTextCtrl


class ExpandoTextView(ExpandoTextCtrl):
    def __init__(self, parent, id=-1, value="",
                 style=wx.TE_READONLY | wx.BORDER_NONE, name=u"BodyText"):
        ExpandoTextCtrl.__init__(self, parent, id, value, wx.DefaultPosition,
                                 wx.DefaultSize, style, wx.DefaultValidator, name)
        # self.SetBackgroundColour(wx.GREEN)
        # self.UseExtraHeight(False)

        self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouseEvent)
        self.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)

    def OnMouseEvent(self, event):
        if event.Moving():
            self.SetCursor(wx.STANDARD_CURSOR)

    def OnSetFocus(self, event):
        self.Navigate(wx.NavigationKeyEvent.IsForward)


class MyFrame3(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, style=wx.TE_READONLY | wx.TE_PROCESS_ENTER)
        self.m_textCtrl3.SetValue("1")
        cursor = wx.StockCursor(wx.CURSOR_ARROW)
        caret = wx.Caret(window=self.m_textCtrl3,size= wx.DefaultSize)
        self.m_textCtrl3.SetCaret(caret)
        self.m_textCtrl3.GetCaret().Hide()

        self.m_textCtrl3.SetCursor(cursor)

        bSizer9.Add(self.m_textCtrl3, 0, wx.ALL, 5)

        view = wx.StaticLine(self)
        view.SetLabel("1212")
        bSizer9.Add(view)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        self.m_staticText1.SetLabel("1212")

        bSizer9.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.SetSizer(bSizer9)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


app = wx.App(False)
frame = MyFrame3(None)
frame.Show(True)
app.MainLoop()
