#!/usr/bin/python

import wx
import os.path as join

class mainApp(wx.App):
    def __init__(self, redirect=False, filename=None):
        self.xPos = 50
        wx.App.__init__(self, redirect, filename)
        self.mainFrame = wx.Frame(None, wx.ID_ANY, title = 'Test Window', pos =(0, 0), size = (800, 600))
        self.mainFrame.SetBackgroundColour('WHITE')
        self.mainFrame.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))

        
        self.mainPanel = wx.Panel(self.mainFrame, wx.ID_ANY, pos=(0, 0), size=(800, 600))
        self.mainPanel.SetBackgroundColour('WHITE')
        ### Write all codes here
        self.testImg = wx.Bitmap('right.png', wx.BITMAP_TYPE_PNG)
        self.testStat = wx.StaticBitmap(self.mainPanel, wx.ID_ANY, self.testImg, (330,100), (self.testImg.GetWidth(), self.testImg.GetHeight()))
        self.testStat.SetBackgroundColour('CYAN')
        self.testButton = wx.Button(self.mainPanel, wx.ID_ANY, "test button", pos=(100,100), size=(100,30))
        self.testButton.Bind(wx.EVT_BUTTON, self.OnButton)
        ### End all codes here
        self.mainFrame.Show(True)

    def OnButton(self, event):
        self.testStat.SetBackgroundColour('WHITE')

def rotateImage(image):
    newImage = ''
    return newImage
        
if __name__ == '__main__':
    app = mainApp()
    app.MainLoop()
