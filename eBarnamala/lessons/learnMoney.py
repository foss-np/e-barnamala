import wx
import wx.lib.statbmp as statbmp
import utils.slideShowUtils  as eUtils
import utils.bottomMenu as bottomMenu
import conf.config as config
import conf.loadDataMoney as loadData
import conf.messages as messages
from os.path import join

class learnMoneyPanel(wx.Panel):
    def __init__(self, parent, id, mainPanel):
        if wx.Platform != "__WXGTK__":
            imgBmp = wx.StaticBitmap
        else:
            imgBmp = statbmp.GenStaticBitmap
        self.currentImg = ''
        self.currentPosition = 0
        self.mainWin = mainPanel
        self.currentSSpath = config.notesImagesPath
        self.blankImg = join(config.coreImagesPath, 'blank220.png')
        self.dataListEnglish = loadData.notesNameEnglish
        self.dataListNepali = loadData.notesNameNepali

        self.menuPanel = wx.Panel(parent, wx.ID_ANY, (0, 0), (800, 100))
        self.menuPanel.SetBackgroundColour(config.backgroundColour)

        notesImg = wx.Bitmap(join(config.buttonsPath,'learnNotes.png'), wx.BITMAP_TYPE_PNG)
        self.notesButton = wx.BitmapButton(self.menuPanel, wx.ID_ANY, notesImg, (50,10), style = wx.NO_BORDER)
        self.notesButton.SetBackgroundColour(config.backgroundColour)
        self.notesButton.Bind(wx.EVT_BUTTON, self.OnNotesButton, id=self.notesButton.GetId())

        coinsImg = wx.Bitmap(join(config.buttonsPath,'learnCoins.png'), wx.BITMAP_TYPE_PNG)
        self.coinsButton = wx.BitmapButton(self.menuPanel, wx.ID_ANY, coinsImg, (200,10), style = wx.NO_BORDER)
        self.coinsButton.SetBackgroundColour(config.backgroundColour)
        self.coinsButton.Bind(wx.EVT_BUTTON, self.OnCoinsButton, id=self.coinsButton.GetId())

        self.displayPanel = wx.Panel(parent, -1, (0, 100), (800, 500))
        self.displayPanel.SetBackgroundColour(config.backgroundColour)
        self.displayPanel.SetFocus()

        self.displayType = wx.StaticText(self.displayPanel, -1, messages.notes, (270, 10), style = wx.ALIGN_CENTRE)
        self.displayType.SetFont(wx.Font(config.fontSize[2], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayType.SetBackgroundColour(config.backgroundColour)

        self.displayText = wx.StaticText(self.displayPanel, -1, self.dataListNepali[self.currentPosition], (50, 100), style = wx.ALIGN_CENTRE)
        self.displayText.SetFont(wx.Font(config.fontSize[2], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText.SetBackgroundColour(config.backgroundColour)

        self.frontBackText = wx.StaticText(self.displayPanel, wx.ID_ANY, messages.back, (490, 59), style = wx.ALIGN_CENTRE)
        self.frontBackText.SetFont(wx.Font(config.fontSize[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.frontBackText.SetBackgroundColour(config.backgroundColour)

        currentImg = join(self.currentSSpath, (self.dataListEnglish[self.currentPosition] + ".png"))
        self.currentImg = currentImg
        displayImg = wx.Bitmap(currentImg, wx.BITMAP_TYPE_PNG)
        self.displayImage = imgBmp(self.displayPanel, -1, displayImg, (330,110), (displayImg.GetWidth(), displayImg.GetHeight()))
        self.displayImage.Bind(wx.EVT_LEFT_DOWN, self.OnChangeFace, id=self.displayImage.GetId())
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

    def OnChangeFace(self, event):
        tempImg = ''
        if self.currentImg.find('Front') != -1:
            tempImg = self.currentImg.replace('Front','Back')
            self.frontBackText.SetLabel(messages.back)
        if self.currentImg.find('Back') != -1:
            tempImg = self.currentImg.replace('Back','Front')
            self.frontBackText.SetLabel(messages.front)
        self.currentImg = tempImg
        tempBitmap = wx.Bitmap(tempImg, wx.BITMAP_TYPE_PNG)
        self.displayImage.SetSize((tempBitmap.GetWidth(), tempBitmap.GetHeight()))
        self.displayImage.SetBitmap(tempBitmap)

    def OnNotesButton(self, event):
        self.currentSSpath = config.notesImagesPath
        self.dataListEnglish = loadData.notesNameEnglish
        self.dataListNepali = loadData.notesNameNepali
        self.currentPosition = -1
        self.currentPosition = eUtils.nextSlide(self.currentPosition, len(self.dataListEnglish))
        self.displayText.SetLabel(self.dataListNepali[self.currentPosition])
        currentImg = join(self.currentSSpath, (self.dataListEnglish[self.currentPosition] + ".png"))
        self.currentImg = currentImg
        self.displayImage.SetPosition((330,100))
        tempBitmap = wx.Bitmap(currentImg, wx.BITMAP_TYPE_PNG)
        self.displayImage.SetSize((tempBitmap.GetWidth(), tempBitmap.GetHeight()))
        self.displayImage.SetBitmap(tempBitmap)
        self.displayType.SetLabel(messages.notes)
    
    def OnCoinsButton(self, event):
        self.currentSSpath = config.coinsImagesPath
        self.dataListEnglish = loadData.coinsNameEnglish
        self.dataListNepali = loadData.coinsNameNepali
        self.currentPosition = -1
        self.currentPosition = eUtils.nextSlide(self.currentPosition, len(self.dataListEnglish))
        self.displayText.SetLabel(self.dataListNepali[self.currentPosition])
        currentImg = join(self.currentSSpath, (self.dataListEnglish[self.currentPosition] + ".png"))
        self.currentImg = currentImg
        self.displayImage.SetPosition((450,120))
        tempBitmap = wx.Bitmap(currentImg, wx.BITMAP_TYPE_PNG)
        self.displayImage.SetSize((tempBitmap.GetWidth(), tempBitmap.GetHeight()))
        self.displayImage.SetBitmap(tempBitmap)
        self.displayType.SetLabel(messages.coins)

    def OnNextArrow(self, event):
        self.currentPosition = eUtils.nextSlide(self.currentPosition, len(self.dataListEnglish))
        self.displayText.SetLabel(self.dataListNepali[self.currentPosition])
        currentImg = join(self.currentSSpath, (self.dataListEnglish[self.currentPosition] + ".png"))
        self.currentImg = currentImg
        self.displayImage.SetBitmap(wx.Bitmap(currentImg, wx.BITMAP_TYPE_PNG))
        self.frontBackText.SetLabel(messages.front)
        
    def OnPreviousArrow(self, event):
        self.currentPosition = eUtils.previousSlide(self.currentPosition, len(self.dataListEnglish))
        self.displayText.SetLabel(self.dataListNepali[self.currentPosition])
        currentImg = join(self.currentSSpath, (self.dataListEnglish[self.currentPosition] + ".png"))
        self.currentImg = currentImg
        self.displayImage.SetBitmap(wx.Bitmap(currentImg, wx.BITMAP_TYPE_PNG))
        self.frontBackText.SetLabel(messages.front)
