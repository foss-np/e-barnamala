import wx

class PaintEvent(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

        self.count = 0
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Centre()
        self.Show(True)

    def OnPaint(self, event):
        self.count = self.count + 1
        print self.count


app = wx.App()
PaintEvent(None, -1, 'paintevent.py')
app.MainLoop()
