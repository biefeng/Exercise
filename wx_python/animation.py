#!usr/bin/env python
# -*- coding: utf-8 -*-
# fileName: animation.py
# time: 2020/07/16 21:06

__author__ = '33504'

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
import wx.adv
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

		animation = wx.adv.Animation()
		animation.LoadFile("F:\\download\\1594905864743.gif")
		animation_ctrl = wx.adv.AnimationCtrl(self, wx.ID_ANY, anim=animation, pos=wx.DefaultPosition)
		animation_ctrl.Play()
		bSizer9.Add(animation_ctrl, 0, wx.ALL, 5)
		self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, style=wx.TE_READONLY | wx.TE_PROCESS_ENTER)
		self.m_textCtrl3.SetValue("1")

		bSizer9.Add(self.m_textCtrl3, 0, wx.ALL, 5)

		self.SetSizer(bSizer9)
		self.Layout()

		self.Centre(wx.BOTH)

	def __del__(self):
		pass


app = wx.App(False)
frame = MyFrame3(None)
frame.Show(True)
app.MainLoop()
