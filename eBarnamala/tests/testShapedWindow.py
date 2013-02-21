#!/usr/bin/python

import wx

class mainApp(wx.App):
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        
        self.mainFrame = wx.Frame(None, wx.ID_ANY, title = 'eBarnamala', pos =(0, 0), style = wx.FRAME_SHAPED|wx.SIMPLE_BORDER|wx.FRAME_NO_TASKBAR|wx.STAY_ON_TOP)
        self.mainFrame.hasShape = False
        self.delta = (0,0)

        self.mainFrame.Bind(wx.EVT_RIGHT_UP, self.OnExit)
        self.mainFrame.Bind(wx.EVT_PAINT, self.OnPaint)

        self.bckGnd = wx.Bitmap('Vippi.png',wx.BITMAP_TYPE_PNG)
        w, h = self.bckGnd.GetWidth(), self.bckGnd.GetHeight()
        self.mainFrame.SetClientSize((w,h))
        self.SetWindowShape()

        dc = wx.ClientDC(self.mainFrame)
        dc.DrawBitmap(self.bckGnd, 0,0, True)

        self.mainFrame.Show(True)

    def OnPaint(self, evt):
        dc = wx.PaintDC(self.mainFrame)
        dc.DrawBitmap(self.bckGnd, 0,0, True)

    def SetWindowShape(self):
        # Use the bitmap's mask to determine the region
        r = wx.RegionFromBitmap(self.bckGnd)
        self.hasShape = self.mainFrame.SetShape(r)

    def OnExit(self, event):
        self.mainFrame.Close()
     
if __name__ == '__main__':
    app = mainApp()
    app.MainLoop()
