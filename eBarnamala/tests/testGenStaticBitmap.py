#!/usr/bin/env python import wx

import wx
import wx.lib.statbmp as statbmp

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.panel = wx.Panel(self, wx.ID_ANY, pos=(0, 0), size=(500, 500))
        self.panel.SetBackgroundColour('BLACK')
        bmp = wx.Bitmap("right.png")
        self.Image = statbmp.GenStaticBitmap(self.panel, wx.ID_ANY, bmp)
        self.Image.Bind(wx.EVT_LEFT_DOWN, self.OnClick)
        S = wx.BoxSizer(wx.VERTICAL)
        S.Add(self.Image, 0)
        self.SetSizerAndFit(S)

    def OnClick(self, event):
        print "Image: was clicked at: %i, %i "%(event.GetX(), event.GetY())

class App(wx.App):
    def OnInit(self):
        frame = MainFrame(None, title= "wxWindowBitmap Test")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

app = App(0)
app.MainLoop() 
