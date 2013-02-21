#!/usr/bin/python

import wx
import Image
import os.path as join

class mainApp(wx.App):
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        self.mainFrame = wx.Frame(None, wx.ID_ANY, title = 'Test Window', pos =(0, 0), size = (800, 600))
        self.mainFrame.SetBackgroundColour('WHITE')
        self.mainFrame.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        
        self.mainPanel = wx.Panel(self.mainFrame, wx.ID_ANY, pos=(0, 0), size=(800, 600))
        self.mainPanel.SetBackgroundColour('WHITE')
        ### Write all codes here
##        sourceImg = Image.open('cow.png')
##        splashImg = wx.EmptyImage(200, 200)
##        sourceImg = sourceImg.resize((200, 200), Image.BILINEAR)
##        splashImg.SetData(sourceImg.convert('RGB').tostring())
##        displayImg = wx.BitmapFromImage(splashImg)
##        self.splashImage = wx.StaticBitmap(self.mainPanel, wx.ID_ANY, displayImg, (420,110), (200, 200))
        
        sourceImg = Image.open( 'orange.png')
        xsize, ysize = sourceImg.size
        imageToDisplay = Image.open('blank.png')
        testImg = wx.Bitmap('blank.png', wx.BITMAP_TYPE_PNG)
        self.splashImage = wx.StaticBitmap(self.mainPanel, wx.ID_ANY, testImg, (420,110), (testImg.GetWidth(), testImg.GetHeight()))
        numberReq = 20
        currentXPos, currentYPos = 10, 10
        posCounter = 0
        for i in range(numberReq):
            imageToDisplay.paste(sourceImg.convert('RGB'), (currentXPos, currentYPos))
            if posCounter < 4:
                posCounter = posCounter + 1
                currentXPos = currentXPos + 30
                currentYPos = currentYPos
            else:
                posCounter = 0
                currentXPos = 10
                currentYPos = currentYPos + 40
        splashImg = wx.EmptyImage(160, 160)
        splashImg.SetData(imageToDisplay.convert('RGB').tostring())
        displayImg = wx.BitmapFromImage(splashImg)
        self.splashImage.SetBitmap(displayImg)
        
        ### End all codes here
        self.mainFrame.Show(True)
        
if __name__ == '__main__':
    app = mainApp()
    app.MainLoop()
