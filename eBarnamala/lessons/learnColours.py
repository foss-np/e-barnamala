import wx
import utils.slideShowUtils  as eUtils
import utils.bottomMenu as bottomMenu
import conf.config as config
import conf.loadDataColours as loadData
import conf.messages as messages
from os.path import join

class learnColoursPanel(wx.Panel):
    def __init__(self, parent, id, mainPanel):
        self.currentPosition = 0
        self.mainWin = mainPanel
        self.currentSSpath = config.colourImagesPath
        self.blankImg = join(config.coreImagesPath, 'blank220.png')
        self.dataListEnglish = loadData.colourNameEnglish
        self.dataListNepali = loadData.colourNameNepali

        self.menuPanel = wx.Panel(parent, -1, (0, 0), (800, 100))
        self.menuPanel.SetBackgroundColour(config.backgroundColour)

        self.displayPanel = wx.Panel(parent, -1, (0, 100), (800, 500))
        self.displayPanel.SetBackgroundColour(config.backgroundColour)

        self.displayType = wx.StaticText(self.displayPanel, -1, messages.colours, (270, 10), style = wx.ALIGN_CENTRE)
        self.displayType.SetFont(wx.Font(config.fontSize[2], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayType.SetBackgroundColour(config.backgroundColour)

        self.displayText = wx.StaticText(self.displayPanel, -1, self.dataListNepali[self.currentPosition], (50, 100), style = wx.ALIGN_CENTRE)
        self.displayText.SetFont(wx.Font(config.fontSize[2], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText.SetBackgroundColour(config.backgroundColour)
        
        currentImg = join(self.currentSSpath, (self.dataListEnglish[self.currentPosition] + ".png"))
        displayImg = wx.Bitmap(currentImg, wx.BITMAP_TYPE_PNG)
        self.displayImage = wx.StaticBitmap(self.displayPanel, -1, displayImg, (500,100), (displayImg.GetWidth(), displayImg.GetHeight()))
        self.displayImage.SetBackgroundColour(config.backgroundColour)

        previousArrowImg = wx.Bitmap(join(config.coreImagesPath,'previousArrow.png'), wx.BITMAP_TYPE_PNG)
        self.previousArrowButton = wx.BitmapButton(self.displayPanel, 6, previousArrowImg, (50,0), style = wx.NO_BORDER)
        self.previousArrowButton.SetBackgroundColour(config.backgroundColour)
        self.previousArrowButton.Bind(wx.EVT_BUTTON, self.OnPreviousArrow, id=6)

        nextArrowImg = wx.Bitmap(join(config.coreImagesPath,'nextArrow.png'), wx.BITMAP_TYPE_PNG)
        self.nextArrowButton = wx.BitmapButton(self.displayPanel, 7, nextArrowImg, (650,0), style = wx.NO_BORDER)
        self.nextArrowButton.SetBackgroundColour(config.backgroundColour)
        self.nextArrowButton.Bind(wx.EVT_BUTTON, self.OnNextArrow, id=7)

        bottomMenu.bottomMenu([self.displayPanel, self.menuPanel], parent, self.mainWin, 'twoButton')

    def OnNextArrow(self, event):
        self.currentPosition = eUtils.nextSlide(self.currentPosition, len(self.dataListEnglish))
        self.displayText.SetLabel(self.dataListNepali[self.currentPosition])
        currentImg = join(self.currentSSpath, (self.dataListEnglish[self.currentPosition] + ".png"))
        self.displayImage.SetBitmap(wx.Bitmap(currentImg, wx.BITMAP_TYPE_PNG))
        
    def OnPreviousArrow(self, event):
        self.currentPosition = eUtils.previousSlide(self.currentPosition, len(self.dataListEnglish))
        self.displayText.SetLabel(self.dataListNepali[self.currentPosition])
        currentImg = join(self.currentSSpath, (self.dataListEnglish[self.currentPosition] + ".png"))
        self.displayImage.SetBitmap(wx.Bitmap(currentImg, wx.BITMAP_TYPE_PNG))
