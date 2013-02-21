import wx
import utils.eUtils  as eUtils
import utils.bottomMenu as bottomMenu
import conf.config as config
import conf.messages as messages
from os.path import join

class learnLettersPanel(wx.Panel):
    def __init__(self, parent, id, mainPanel):
        self.currentLesson = "kaKha"
        self.charPosition = 0
        self.mainWin = mainPanel
        self.imgInfo = [0,0]    #track img displayed. [0] for letter-img and [1] for within same letter
        self.blankImg = join(config.coreImagesPath, 'blank.png')

        currentChar, self.charPosition = eUtils.nextLetter(self.currentLesson, wx.ID_ANY)
        imgToDisplay, imgNameToDisplay, self.imgInfo = eUtils.nextImage(self.currentLesson, self.imgInfo)

        self.menuPanel = wx.Panel(parent, wx.ID_ANY, (0, 0), (800, 100))
        self.menuPanel.SetBackgroundColour(config.backgroundColour)
        self.menuPanel.SetFocus()

        self.displayPanel = wx.Panel(parent, wx.ID_ANY, (0, 100), (800, 500))
        self.displayPanel.SetBackgroundColour(config.backgroundColour)
        self.displayPanel.SetFocus()
        
        aaaImg = wx.Bitmap(join(config.buttonsPath,'aaa.png'), wx.BITMAP_TYPE_PNG)
        self.aaaButton = wx.BitmapButton(self.menuPanel, wx.ID_ANY, aaaImg, (50,10), style = wx.NO_BORDER)
        self.aaaButton.SetBackgroundColour(config.backgroundColour)
        self.aaaButton.Bind(wx.EVT_BUTTON, self.OnAaaLetters, id=self.aaaButton.GetId())

        kaKhaImg = wx.Bitmap(join(config.buttonsPath,'kakha.png'), wx.BITMAP_TYPE_PNG)
        self.kaKhaButton = wx.BitmapButton(self.menuPanel, wx.ID_ANY, kaKhaImg, (200,10), style = wx.NO_BORDER)
        self.kaKhaButton.SetBackgroundColour(config.backgroundColour)
        self.kaKhaButton.Bind(wx.EVT_BUTTON, self.OnKaKhaLetters, id=self.kaKhaButton.GetId())

        baraKhariImg = wx.Bitmap(join(config.buttonsPath,'baraKhari.png'), wx.BITMAP_TYPE_PNG)
        self.baraKhariButton = wx.BitmapButton(self.menuPanel, wx.ID_ANY, baraKhariImg, (350,10), style = wx.NO_BORDER)
        self.baraKhariButton.SetBackgroundColour(config.backgroundColour)
        self.baraKhariButton.Bind(wx.EVT_BUTTON, self.OnBaraKhariLetters, id=self.baraKhariButton.GetId())

        oneTwoImg = wx.Bitmap(join(config.buttonsPath,'12.png'), wx.BITMAP_TYPE_PNG)
        self.oneTwoButton = wx.BitmapButton(self.menuPanel, wx.ID_ANY, oneTwoImg, (500,10), style = wx.NO_BORDER)
        self.oneTwoButton.SetBackgroundColour(config.backgroundColour)
        self.oneTwoButton.Bind(wx.EVT_BUTTON, self.OnOneTwoLetters, id=self.oneTwoButton.GetId())

        elevenTwelveImg = wx.Bitmap(join(config.buttonsPath,'elevenTwelve.png'), wx.BITMAP_TYPE_PNG)
        self.elevenTwelveButton = wx.BitmapButton(self.menuPanel, wx.ID_ANY, elevenTwelveImg, (650,10), style = wx.NO_BORDER)
        self.elevenTwelveButton.SetBackgroundColour(config.backgroundColour)
        self.elevenTwelveButton.Bind(wx.EVT_BUTTON, self.OnElevenTwelveLetters, id=self.elevenTwelveButton.GetId())

        self.displayType = wx.StaticText(self.displayPanel, wx.ID_ANY, messages.byanjanBarna, (270, 10), style = wx.ALIGN_CENTRE)
        self.displayType.SetFont(wx.Font(config.fontSize[2], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))

        self.displayText = wx.StaticText(self.displayPanel, wx.ID_ANY, currentChar, (50, 90), style = wx.ALIGN_CENTRE)
        self.displayText.SetFont(wx.Font(config.fontSize[6], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))

        self.displayName = wx.StaticText(self.displayPanel, wx.ID_ANY, imgNameToDisplay, (600, 110), style = wx.ALIGN_CENTRE)
        self.displayName.SetFont(wx.Font(config.fontSize[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))

        displayImg = wx.Bitmap(imgToDisplay, wx.BITMAP_TYPE_PNG)
        self.displayImage = wx.StaticBitmap(self.displayPanel, wx.ID_ANY, displayImg, (500,150), (displayImg.GetWidth(), displayImg.GetHeight()))

        previousArrowImg = wx.Bitmap(join(config.coreImagesPath,'previousArrow.png'), wx.BITMAP_TYPE_PNG)
        self.previousArrowButton = wx.BitmapButton(self.displayPanel, wx.ID_ANY, previousArrowImg, (50,0), style = wx.NO_BORDER)
        self.previousArrowButton.SetBackgroundColour(config.backgroundColour)
        self.previousArrowButton.Bind(wx.EVT_BUTTON, self.OnPreviousArrow, id=self.previousArrowButton.GetId())

        nextArrowImg = wx.Bitmap(join(config.coreImagesPath,'nextArrow.png'), wx.BITMAP_TYPE_PNG)
        self.nextArrowButton = wx.BitmapButton(self.displayPanel, wx.ID_ANY, nextArrowImg, (650,0), style = wx.NO_BORDER)
        self.nextArrowButton.SetBackgroundColour(config.backgroundColour)
        self.nextArrowButton.Bind(wx.EVT_BUTTON, self.OnNextArrow, id=self.nextArrowButton.GetId())

        nextWordImg = wx.Bitmap(join(config.buttonsPath,'vocabButton.png'), wx.BITMAP_TYPE_PNG)
        self.nextWordButton = wx.BitmapButton(self.displayPanel, wx.ID_ANY, nextWordImg, (500,320), style = wx.NO_BORDER)
        self.nextWordButton.SetBackgroundColour(config.backgroundColour)
        self.nextWordButton.Bind(wx.EVT_BUTTON, self.OnNextWord, id=self.nextWordButton.GetId())

        bottomMenu.bottomMenu([self.displayPanel, self.menuPanel], parent, self.mainWin, 'twoButton')
        
    def OnBaraKhariLetters(self, event):
        displayStr = messages.heading + "\n"
        self.currentLesson = "barakhari"
        self.displayType.SetLabel(messages.barakhari)
        self.displayImage.Show(False)
        self.displayName.Show(False)
        self.nextWordButton.Show(False)
        charSplit = lambda currentStr : currentStr.split("-")
        currentChar, self.charPosition = eUtils.nextBarakhariCombo(self.currentLesson, -1)
        self.displayText.SetFont(wx.Font(config.fontSizeForBarakhari[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        for i in currentChar: 
            chars = charSplit(i)
            displayStr = displayStr + (chars[0] + "  " + messages.plusSign + "  " + chars[1] + "  " + messages.plusSign + "  " + chars[2] + "  " + messages.equalSign + "    " + chars[3])
            displayStr = displayStr + "\n"
        self.displayText.SetPosition((120, 120))
        self.displayText.SetLabel(displayStr)
        
    def OnAaaLetters(self, event):
        self.displayImage.Show(True)
        self.displayName.Show(True)
        self.nextWordButton.Show(True)
        self.displayText.SetFont(wx.Font(config.fontSize[6], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayName.SetFont(wx.Font(config.fontSize[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.currentLesson = "aaa"
        self.charPosition = 0
        self.imgInfo[0] = 0
        self.imgInfo[1] = 0
        currentChar, self.charPosition = eUtils.nextLetter(self.currentLesson, -1)
        self.displayType.SetLabel(messages.sworBarna)
        self.displayText.SetLabel(currentChar)
        imgToDisplay, imgNameToDisplay, self.imgInfo = eUtils.nextImage(self.currentLesson, self.imgInfo)
        self.displayName.SetLabel(imgNameToDisplay)
        if imgToDisplay != '':
            self.displayImage.SetBitmap(wx.Bitmap(imgToDisplay, wx.BITMAP_TYPE_PNG))
            self.nextWordButton.Show(True)
        else:
            self.displayImage.SetBitmap(wx.Bitmap(self.blankImg, wx.BITMAP_TYPE_PNG))
            self.nextWordButton.Show(False)

    def OnKaKhaLetters(self, event):
        self.displayImage.Show(True)
        self.displayName.Show(True)
        self.nextWordButton.Show(True)
        self.displayText.SetFont(wx.Font(config.fontSize[6], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.currentLesson = "kaKha"
        self.charPosition = 0
        self.imgInfo[0] = 0
        self.imgInfo[1] = 0
        currentChar, self.charPosition = eUtils.nextLetter(self.currentLesson, -1)
        self.displayType.SetLabel(messages.byanjanBarna)
        self.displayText.SetLabel(currentChar)
        imgToDisplay, imgNameToDisplay, self.imgInfo = eUtils.nextImage(self.currentLesson, self.imgInfo)
        self.displayName.SetLabel(imgNameToDisplay)
        if imgToDisplay != '':
            self.displayImage.SetBitmap(wx.Bitmap(imgToDisplay, wx.BITMAP_TYPE_PNG))
            self.nextWordButton.Show(True)
        else:
            self.displayImage.SetBitmap(wx.Bitmap(self.blankImg, wx.BITMAP_TYPE_PNG))
            self.nextWordButton.Show(False)

    def OnOneTwoLetters(self, event):
        self.displayImage.Show(True)
        self.displayName.Show(True)
        self.nextWordButton.Show(False)
        self.displayText.SetFont(wx.Font(config.fontSize[6], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.currentLesson = "oneTwo"
        self.charPosition = 0
        self.imgInfo[0] = 0
        self.imgInfo[1] = 0
        currentChar, self.charPosition = eUtils.nextLetter(self.currentLesson, -1)
        self.displayType.SetLabel(messages.numbers)
        self.displayText.SetLabel(currentChar)
        imgToDisplay, imgNameToDisplay, self.imgInfo = eUtils.nextImage(self.currentLesson, self.imgInfo)
        self.displayName.SetLabel(imgNameToDisplay)
        self.nextWordButton.Show(False)
        if imgToDisplay != '':
            self.displayImage.SetBitmap(wx.Bitmap(imgToDisplay, wx.BITMAP_TYPE_PNG))
            #self.nextWordButton.Show(True)
        else:
            self.displayImage.SetBitmap(wx.Bitmap(self.blankImg, wx.BITMAP_TYPE_PNG))
            #self.nextWordButton.Show(False)

    def OnElevenTwelveLetters(self, event):
        self.currentLesson = "elevenTwelve"
        self.nextWordButton.Show(False)
        self.displayText.SetFont(wx.Font(config.fontSize[6], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        currentChar, self.charPosition = eUtils.nextLetter(self.currentLesson, -1)
        self.displayType.SetLabel(messages.numbers)
        self.displayText.SetLabel(currentChar)
        imgToDisplayTemp, numberName = eUtils.nextAboveNineImage(self.currentLesson, currentChar)
        self.displayName.SetLabel(numberName)
        self.displayImage.SetBitmap(wx.BitmapFromImage(imgToDisplayTemp))
        
    def OnNextArrow(self, event):
        if self.currentLesson == "barakhari":
            displayStr = messages.heading + "\n"
            self.currentLesson = "barakhari"
            self.displayType.SetLabel(messages.barakhari)
            self.displayImage.Show(False)
            self.displayName.Show(False)
            self.nextWordButton.Show(False)
            charSplit = lambda currentStr : currentStr.split("-")
            currentChar, self.charPosition = eUtils.nextBarakhariCombo(self.currentLesson, self.charPosition)
            self.displayText.SetFont(wx.Font(config.fontSizeForBarakhari[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
            for i in currentChar:
                chars = charSplit(i)
                displayStr = displayStr + (chars[0] + "  " + messages.plusSign + "  " + chars[1] + "  " + messages.plusSign + "  " + chars[2] + "  " + messages.equalSign + "    " + chars[3])
                displayStr = displayStr + "\n"            
            self.displayText.SetLabel(displayStr)
        else:
            currentChar, self.charPosition = eUtils.nextLetter(self.currentLesson, self.charPosition)
            self.displayText.SetLabel(currentChar)
            self.imgInfo[0] = self.charPosition
            self.imgInfo[1] = 0
            imgToDisplay, imgNameToDisplay, self.imgInfo = eUtils.nextImage(self.currentLesson, self.imgInfo)
            self.displayName.SetLabel(imgNameToDisplay)
            if imgToDisplay != '':
                self.displayImage.SetBitmap(wx.Bitmap(imgToDisplay, wx.BITMAP_TYPE_PNG))
                self.nextWordButton.Show(True)
            else:
                self.displayImage.SetBitmap(wx.Bitmap(self.blankImg, wx.BITMAP_TYPE_PNG))
                self.nextWordButton.Show(False)
            if self.currentLesson == "oneTwo":
                self.nextWordButton.Show(False)
            if self.currentLesson == "elevenTwelve":
                self.nextWordButton.Show(False)
                imgToDisplayTemp, numberName = eUtils.nextAboveNineImage(self.currentLesson, currentChar)
                self.displayName.SetLabel(numberName)
                self.displayImage.SetBitmap(wx.BitmapFromImage(imgToDisplayTemp))
        
    def OnPreviousArrow(self, event):
        if self.currentLesson == "barakhari":
            displayStr = messages.heading + "\n"
            self.currentLesson = "barakhari"
            self.displayType.SetLabel(messages.barakhari)
            self.displayImage.Show(False)
            self.displayName.Show(False)
            self.nextWordButton.Show(False)
            charSplit = lambda currentStr : currentStr.split("-")
            currentChar, self.charPosition = eUtils.previousBarakhariCombo(self.currentLesson, self.charPosition)
            self.displayText.SetFont(wx.Font(config.fontSizeForBarakhari[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
            for i in currentChar: 
                chars = charSplit(i)
                displayStr = displayStr + (chars[0] + "  " + messages.plusSign + "  " + chars[1] + "  " + messages.plusSign + "  " + chars[2] + "  " + messages.equalSign + "    " + chars[3])
                displayStr = displayStr + "\n"            
            self.displayText.SetLabel(displayStr)
        else:
            currentChar, self.charPosition = eUtils.previousLetter(self.currentLesson, self.charPosition)
            self.displayText.SetLabel(currentChar)
            self.imgInfo[0] = self.charPosition
            self.imgInfo[1] = 0
            imgToDisplay, imgNameToDisplay, self.imgInfo = eUtils.nextImage(self.currentLesson, self.imgInfo)
            self.displayName.SetLabel(imgNameToDisplay)
            if imgToDisplay != '':
                self.displayImage.SetBitmap(wx.Bitmap(imgToDisplay, wx.BITMAP_TYPE_PNG))
                self.nextWordButton.Show(True)
            else:
                self.displayImage.SetBitmap(wx.Bitmap(self.blankImg, wx.BITMAP_TYPE_PNG))
                self.nextWordButton.Show(False)
            if self.currentLesson == "oneTwo":
                self.nextWordButton.Show(False)
            if self.currentLesson == "elevenTwelve":
                self.nextWordButton.Show(False)
                imgToDisplayTemp, numberName = eUtils.nextAboveNineImage(self.currentLesson, currentChar)
                self.displayName.SetLabel(numberName)
                self.displayImage.SetBitmap(wx.BitmapFromImage(imgToDisplayTemp))

    def OnNextWord(self, event):
        imgToDisplay, imgNameToDisplay, self.imgInfo = eUtils.nextWordImage(self.currentLesson, self.imgInfo)
        self.displayName.SetLabel(imgNameToDisplay)
        if imgToDisplay != '':
            self.displayImage.SetBitmap(wx.Bitmap(imgToDisplay, wx.BITMAP_TYPE_PNG))
        else:
            self.displayImage.SetBitmap(wx.Bitmap(self.blankImg, wx.BITMAP_TYPE_PNG))
        
