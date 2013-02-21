#!/usr/bin/python

import wx
import os.path as join
import Image, ImageDraw 

class mainApp(wx.App):
    def __init__(self, redirect=False, filename=None):
        self.xPos = 50
        wx.App.__init__(self, redirect, filename)
        self.mainFrame = wx.Frame(None, wx.ID_ANY, title = 'Test Window', pos =(0, 0), size = (800, 600))
        self.mainFrame.SetBackgroundColour('WHITE')
        self.mainFrame.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))

        
        self.mainPanel = wx.Panel(self.mainFrame, wx.ID_ANY, pos=(0, 0), size=(800, 600))
        self.mainPanel.SetBackgroundColour('GREY')
        ### Write all codes here
        self.imageList = ['right.png']
        self.testImg = wx.BitmapFromImage(resizeImage(self.imageList, 65)[0])
        self.testStat = wx.StaticBitmap(self.mainPanel, wx.ID_ANY, self.testImg, (330,100), (self.testImg.GetWidth(), self.testImg.GetHeight()))
        self.testStat.Bind(wx.EVT_LEFT_DOWN, self.OnButton)
        self.displayText = wx.StaticText(self.mainPanel, wx.ID_ANY, 'cf', (540,25), style = wx.ALIGN_CENTRE)
        self.displayText.SetFont(wx.Font(80, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Aalekh'))
        self.displayText.SetBackgroundColour('WHITE')
        self.displayText.Bind(wx.EVT_LEFT_DOWN, self.OnButton1, id=self.displayText.GetId())
        ### End all codes here
        self.mainFrame.Show(True)

    def OnButton(self, event):
        event.GetEventObject().SetBackgroundColour('PINK')
        #self.testStat.SetBackgroundColour('PINK')
        self.testStat.SetBitmap(self.testImg)
        
    def OnButton1(self, event):
        #self.displayText.SetLabel(event.GetEventObject().GetLabel())
        event.GetEventObject().SetLabel('c')
        self.displayText.SetBackgroundColour('PINK')
        
def resizeImage(imageList, resizePercent):
    newImageList = []
    for i in imageList:
        temp = Image.open(i)
        temp = temp.resize(((resizePercent*temp.size[0])/100,(resizePercent*temp.size[1])/100), Image.ANTIALIAS)
        returnNumberImg = wx.EmptyImage(temp.size[0], temp.size[1])
        returnNumberImg.SetData(temp.convert('RGB').tostring())
        returnNumberImg.SetAlphaData(temp.convert("RGBA").tostring()[3::4])
        newImageList.append(returnNumberImg)
    return newImageList

def drawBorderImage(image, resizePercent=90):
    newImageList = []
    temp = Image.open(image)
    wOld, hOld = temp.size[0], temp.size[1]
    bckgnd = Image.new('RGBA',(wOld, hOld))
    temp = temp.resize(((resizePercent*temp.size[0])/100,(resizePercent*temp.size[1])/100), Image.ANTIALIAS)
    wNew, hNew = temp.size[0], temp.size[1]
    draw = ImageDraw.Draw(bckgnd)
    draw.rectangle([0, 0, wOld, hOld], fill=(255,0,0))
    bckgnd.paste(temp.convert('RGBA'), (int((wOld-wNew)/2), int((hOld-hNew)/2)))
    returnNumberImg = wx.EmptyImage(bckgnd.size[0], bckgnd.size[1])
    returnNumberImg.SetData(bckgnd.convert('RGB').tostring())
    returnNumberImg.SetAlphaData(bckgnd.convert("RGBA").tostring()[3::4])
    return returnNumberImg

        
if __name__ == '__main__':
    app = mainApp()
    app.MainLoop()
