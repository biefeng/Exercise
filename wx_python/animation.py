# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/07/16 18:55
# file_name : animation.py

import wx.adv
import wx


class MyFrame2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        animation = wx.adv.Animation()
        animation.LoadFile("D:\\Download\\download\\1594898894031.gif", wx.adv.ANIMATION_TYPE_ANY)
        self.m_animCtrl1 = wx.adv.AnimationCtrl(self, wx.ID_ANY, animation, wx.DefaultPosition, wx.DefaultSize, wx.adv.AC_DEFAULT_STYLE)

        # self.m_animCtrl1.SetInactiveBitmap(wx.Bitmap(u"D:\\Download\\download\\5f0a1784bef2f3e1f5a404001f76e7a9.gif", wx.BITMAP_TYPE_ANY))
        self.m_animCtrl1.Play()
        bSizer1.Add(self.m_animCtrl1, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


app = wx.App(False)
frame = MyFrame2(None)
frame.Show(True)
app.MainLoop()
