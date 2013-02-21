import wx
import utils.eUtils  as eUtils
import conf.config as config
import conf.messages as messages
from os.path import join

class learnTimePanel(wx.Panel):
    def __init__(self, parent, id, mainPanel):
        self.currentLesson = "time"
        self.charPosition = 0
        self.mainWin = mainPanel
        self.imgInfo = [0,0]
        self.blankImg = join(config.coreImagesPath, 'blank.png')
        self.tempBackString = messages.timeBackString

        currentChar, self.charPosition = eUtils.nextLetter(self.currentLesson, -1)
        imgToDisplay, imgNameToDisplay, self.imgInfo = eUtils.nextImage(self.currentLesson, self.imgInfo)
        
##        self.menuPanel = wx.Panel(parent, -1, (0, 0), (800, 100))
##        self.menuPanel.SetBackgroundColour('WHITE')
##        self.menuPanel.SetFocus()

        self.displayPanel = wx.Panel(parent, -1, (0, 0), (800, 600))
        self.displayPanel.SetBackgroundColour('WHITE')
        self.displayPanel.SetFocus()

        timeText = str(currentChar) + " -" + imgNameToDisplay + "_ " + self.tempBackString[0]
        timeTextEng = str(self.charPosition + 1) + "  " + self.tempBackString[1]

        self.timeText = wx.StaticText(self.displayPanel, -1, messages.timeTitleString, (50, 160), style = wx.ALIGN_CENTRE)
        self.timeText.SetFont(wx.Font(config.fontSize[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        
        self.displayText = wx.StaticText(self.displayPanel, -1, timeText, (120, 220), style = wx.ALIGN_CENTRE)
        self.displayText.SetFont(wx.Font(config.fontSize[1], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))

        self.displayTextEng = wx.StaticText(self.displayPanel, -1, timeTextEng, (120, 290), style = wx.ALIGN_CENTRE)
        self.displayTextEng.SetFont(wx.Font(config.fontSize[1], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontNameEnglish))

        displayImg = wx.Bitmap(imgToDisplay, wx.BITMAP_TYPE_PNG)
        self.displayImage = wx.StaticBitmap(self.displayPanel, -1, displayImg, (500,180), (displayImg.GetWidth(), displayImg.GetHeight()))

        time = ''
        if self.charPosition < 9:
            time = "0" + str(self.charPosition + 1) + " : " + "00"
        else:
            time = str(self.charPosition + 1) + " : " + "00"

        self.displayTime = wx.StaticText(self.displayPanel, -1, time, (500, 360), style = wx.ALIGN_CENTRE)
        self.displayTime.SetFont(wx.Font(config.fontSize[1], wx.SWISS, wx.NORMAL, wx.NORMAL, False, '7 segment'))

        previousArrowImg = wx.Bitmap(join(config.coreImagesPath,'previousArrow.png'), wx.BITMAP_TYPE_PNG)
        self.previousArrowButton = wx.BitmapButton(self.displayPanel, 5, previousArrowImg, (50,60), style = wx.NO_BORDER)
        self.previousArrowButton.SetBackgroundColour('WHITE')
        self.previousArrowButton.Bind(wx.EVT_BUTTON, self.OnPreviousArrow, id=5)

        nextArrowImg = wx.Bitmap(join(config.coreImagesPath,'nextArrow.png'), wx.BITMAP_TYPE_PNG)
        self.nextArrowButton = wx.BitmapButton(self.displayPanel, 6, nextArrowImg, (650,60), style = wx.NO_BORDER)
        self.nextArrowButton.SetBackgroundColour('WHITE')
        self.nextArrowButton.Bind(wx.EVT_BUTTON, self.OnNextArrow, id=6)

        homeImg = wx.Bitmap(join(config.buttonsPath,'home.png'), wx.BITMAP_TYPE_PNG)
        self.homeButton = wx.BitmapButton(self.displayPanel, 8, homeImg, (100,480), style = wx.NO_BORDER)
        self.homeButton.SetBackgroundColour('WHITE')
        self.homeButton.Bind(wx.EVT_BUTTON, self.OnHome, id=8)

    def OnHome(self, event):
        self.displayPanel.Destroy()
        self.mainWin.Show(True)
        self.mainWin.SendSizeEvent()
        
    def OnNextArrow(self, event):
        currentChar, self.charPosition = eUtils.nextLetter(self.currentLesson, self.charPosition)
        self.imgInfo[0] = self.charPosition
        self.imgInfo[1] = 0
        time = ''
        if self.charPosition < 9:
            time = "0" + str(self.charPosition + 1) + " : " + "00"
        else:
            time = str(self.charPosition + 1) + " : " + "00"
        self.displayTime.SetLabel(time)
        imgToDisplay, imgNameToDisplay, self.imgInfo = eUtils.nextImage(self.currentLesson, self.imgInfo)
        timeText = str(currentChar) + " -" + imgNameToDisplay + "_ " + self.tempBackString[0]
        timeTextEng = str(self.charPosition + 1) + "  " + self.tempBackString[1]
        self.displayText.SetLabel(timeText)
        self.displayTextEng.SetLabel(timeTextEng)
        if imgToDisplay != '':
            self.displayImage.SetBitmap(wx.Bitmap(imgToDisplay, wx.BITMAP_TYPE_PNG))
        else:
            self.displayImage.SetBitmap(wx.Bitmap(self.blankImg, wx.BITMAP_TYPE_PNG))
        
    def OnPreviousArrow(self, event):
        currentChar, self.charPosition = eUtils.previousLetter(self.currentLesson, self.charPosition)
        self.imgInfo[0] = self.charPosition
        self.imgInfo[1] = 0
        time = ''
        if self.charPosition < 9:
            time = "0" + str(self.charPosition + 1) + " : " + "00"
        else:
            time = str(self.charPosition + 1) + " : " + "00"
        self.displayTime.SetLabel(time)
        imgToDisplay, imgNameToDisplay, self.imgInfo = eUtils.nextImage(self.currentLesson, self.imgInfo)
        timeText = str(currentChar) + " -" + imgNameToDisplay + "_ " + self.tempBackString[0]
        timeTextEng = str(self.charPosition + 1) + "  " + self.tempBackString[1]
        self.displayText.SetLabel(timeText)
        self.displayTextEng.SetLabel(timeTextEng)
        if imgToDisplay != '':
            self.displayImage.SetBitmap(wx.Bitmap(imgToDisplay, wx.BITMAP_TYPE_PNG))
        else:
            self.displayImage.SetBitmap(wx.Bitmap(self.blankImg, wx.BITMAP_TYPE_PNG))
