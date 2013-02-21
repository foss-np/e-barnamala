import wx
import utils.slideShowUtils  as eUtils
import utils.bottomMenu as bottomMenu
import conf.config as config
import conf.loadDataForTrafficSigns as loadData
import conf.messages as messages
from os.path import join

class learnTrafficSignPanel(wx.Panel):
    def __init__(self, parent, id, mainPanel):
        self.currentLesson = "trafficSign"
        self.currentPosition = 0
        self.mainWin = mainPanel
        self.currentSSpath = config.trafficSignImagesPath
        self.blankImg = join(config.coreImagesPath, 'blank.png')

        self.menuPanel = wx.Panel(parent, -1, (0, 0), (800, 100))
        self.menuPanel.SetBackgroundColour(config.backgroundColour)
        self.menuPanel.SetFocus()

        self.displayPanel = wx.Panel(parent, -1, (0, 100), (800, 500))
        self.displayPanel.SetBackgroundColour(config.backgroundColour)
        self.displayPanel.SetFocus()
        
        self.displayText = wx.StaticText(self.displayPanel, -1, loadData.trafficSignNepali[self.currentPosition], (80, 140), style = wx.ALIGN_CENTRE)
        self.displayText.SetFont(wx.Font(config.fontSize[1], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))

        currentImg = join(self.currentSSpath, (loadData.trafficSignEnglish[self.currentPosition] + ".png"))
        displayImg = wx.Bitmap(currentImg, wx.BITMAP_TYPE_PNG)
        self.displayImage = wx.StaticBitmap(self.displayPanel, -1, displayImg, (500,140), (displayImg.GetWidth(), displayImg.GetHeight()))

        previousArrowImg = wx.Bitmap(join(config.coreImagesPath,'previousArrow.png'), wx.BITMAP_TYPE_PNG)
        self.previousArrowButton = wx.BitmapButton(self.displayPanel, 5, previousArrowImg, (50,0), style = wx.NO_BORDER)
        self.previousArrowButton.SetBackgroundColour(config.backgroundColour)
        self.previousArrowButton.Bind(wx.EVT_BUTTON, self.OnPreviousArrow, id=5)

        nextArrowImg = wx.Bitmap(join(config.coreImagesPath,'nextArrow.png'), wx.BITMAP_TYPE_PNG)
        self.nextArrowButton = wx.BitmapButton(self.displayPanel, 6, nextArrowImg, (650,0), style = wx.NO_BORDER)
        self.nextArrowButton.SetBackgroundColour(config.backgroundColour)
        self.nextArrowButton.Bind(wx.EVT_BUTTON, self.OnNextArrow, id=6)

        bottomMenu.bottomMenu([self.displayPanel, self.menuPanel], parent, self.mainWin, 'twoButton')
        
    def OnNextArrow(self, event):
        self.currentPosition = eUtils.nextSlide(self.currentPosition, len(loadData.trafficSignEnglish))
        self.displayText.SetLabel(loadData.trafficSignNepali[self.currentPosition])
        currentImg = join(self.currentSSpath, (loadData.trafficSignEnglish[self.currentPosition] + ".png"))
        self.displayImage.SetBitmap(wx.Bitmap(currentImg, wx.BITMAP_TYPE_PNG))
        
    def OnPreviousArrow(self, event):
        self.currentPosition = eUtils.previousSlide(self.currentPosition, len(loadData.trafficSignEnglish))
        self.displayText.SetLabel(loadData.trafficSignNepali[self.currentPosition])
        currentImg = join(self.currentSSpath, (loadData.trafficSignEnglish[self.currentPosition] + ".png"))
        self.displayImage.SetBitmap(wx.Bitmap(currentImg, wx.BITMAP_TYPE_PNG))
