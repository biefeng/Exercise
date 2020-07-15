import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1)
        self.panel = wx.Panel(self)
        self.st = wx.StaticText(self.panel, wx.ID_ANY, "Hello, World! Copy me with right click",pos=(5,5))
        self.st.Bind(wx.EVT_RIGHT_DOWN,self.ShowPopup)
        self.tc = wx.TextCtrl(self.panel, wx.ID_ANY, "Paste here", pos=(5,30),size=(300,20))
        self.tc2 = wx.TextCtrl(self.panel, wx.ID_ANY,"TextCtrl masquerading as StaticText - Select me",style=wx.TE_READONLY|wx.NO_BORDER,pos=(5,60),size=(300,20))
        self.tc2.SetBackgroundColour(self.panel.GetBackgroundColour())
        self.Show()

    def ShowPopup(self,event):
        popmenu = wx.Menu()
        popmenu.Append(1, "Copy this text to clipboard")
        popmenu.Bind(wx.EVT_MENU, self.Copy)
        self.panel.PopupMenu(popmenu)
        popmenu.Destroy()

    def Copy(self,event):
        clipdata = wx.TextDataObject()
        text = self.st.GetLabelText()
        clipdata.SetText(text)
        wx.TheClipboard.Open()
        wx.TheClipboard.SetData(clipdata)
        wx.TheClipboard.Close()

app = wx.App()
frame = MyFrame()
app.MainLoop()