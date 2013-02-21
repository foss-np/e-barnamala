import wx
import utils.slideShowUtils  as eUtils
import utils.bottomMenu as bottomMenu
import conf.config as config
import conf.loadDataAnimals as loadData
import conf.messages as messages
from os.path import join

class learnAnimalsPanel(wx.Panel):
    def __init__(self, parent, id, mainPanel):
        self.currentPosition = 0
        self.mainWin = mainPanel
        self.currentSSpath = config.animalImagesPath
        self.blankImg = join(config.coreImagesPath, 'blank220.png')
        self.dataListEnglish = loadData.animalNameEnglish
        self.dataListNepali = loadData.animalNameNepali

        self.menuPanel = wx.Panel(parent, -1, (0, 0), (800, 100))
        self.menuPanel.SetBackgroundColour(config.backgroundColour)

        animalImg = wx.Bitmap(join(config.buttonsPath,'animal.png'), wx.BITMAP_TYPE_PNG)
        self.animalButton = wx.BitmapButton(self.menuPanel, 1, animalImg, (50,10), style = wx.NO_BORDER)
        self.animalButton.SetBackgroundColour(config.backgroundColour)
        self.animalButton.Bind(wx.EVT_BUTTON, self.OnAnimalButton, id=1)

        birdImg = wx.Bitmap(join(config.buttonsPath,'bird.png'), wx.BITMAP_TYPE_PNG)
        self.birdButton = wx.BitmapButton(self.menuPanel, 2, birdImg, (200,10), style = wx.NO_BORDER)
        self.birdButton.SetBackgroundColour(config.backgroundColour)
        self.birdButton.Bind(wx.EVT_BUTTON, self.OnBirdButton, id=2)

        insectImg = wx.Bitmap(join(config.buttonsPath,'insect.png'), wx.BITMAP_TYPE_PNG)
        self.insectButton = wx.BitmapButton(self.menuPanel, 3, insectImg, (350,10), style = wx.NO_BORDER)
        self.insectButton.SetBackgroundColour(config.backgroundColour)
        self.insectButton.Bind(wx.EVT_BUTTON, self.OnInsectButton, id=3)

        domesticImg = wx.Bitmap(join(config.buttonsPath,'domesticAnimals.png'), wx.BITMAP_TYPE_PNG)
        self.domesticButton = wx.BitmapButton(self.menuPanel, 4, domesticImg, (500,10), style = wx.NO_BORDER)
        self.domesticButton.SetBackgroundColour(config.backgroundColour)
        self.domesticButton.Bind(wx.EVT_BUTTON, self.OnDomesticButton, id=4)
        
        wildImg = wx.Bitmap(join(config.buttonsPath,'wildAnimals.png'), wx.BITMAP_TYPE_PNG)
        self.wildButton = wx.BitmapButton(self.menuPanel, 5, wildImg, (650,10), style = wx.NO_BORDER)
        self.wildButton.SetBackgroundColour(config.backgroundColour)
        self.wildButton.Bind(wx.EVT_BUTTON, self.OnWildButton, id=5)

        self.displayPanel = wx.Panel(parent, -1, (0, 100), (800, 500))
        self.displayPanel.SetBackgroundColour(config.backgroundColour)
        self.displayPanel.SetFocus()

        self.displayType = wx.StaticText(self.displayPanel, -1, messages.animal, (270, 10), style = wx.ALIGN_CENTRE)
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

    def OnAnimalButton(self, event):
        self.currentSSpath = config.animalImagesPath
        self.dataListEnglish = loadData.animalNameEnglish
        self.dataListNepali = loadData.animalNameNepali
        self.currentPosition = -1
        self.currentPosition = eUtils.nextSlide(self.currentPosition, len(self.dataListEnglish))
        self.displayText.SetLabel(self.dataListNepali[self.currentPosition])
        currentImg = join(self.currentSSpath, (self.dataListEnglish[self.currentPosition] + ".png"))
        self.displayImage.SetBitmap(wx.Bitmap(currentImg, wx.BITMAP_TYPE_PNG))
        self.displayType.SetLabel(messages.animal)

    def OnDomesticButton(self, event):
        self.currentSSpath = config.animalImagesPath
        self.dataListEnglish = loadData.domesticAnimalEnglish
        self.dataListNepali = loadData.domesticAnimalNepali
        self.currentPosition = -1
        self.currentPosition = eUtils.nextSlide(self.currentPosition, len(self.dataListEnglish))
        self.displayText.SetLabel(self.dataListNepali[self.currentPosition])
        currentImg = join(self.currentSSpath, (self.dataListEnglish[self.currentPosition] + ".png"))
        self.displayImage.SetBitmap(wx.Bitmap(currentImg, wx.BITMAP_TYPE_PNG))
        self.displayType.SetLabel(messages.domesticAnimal)

    def OnWildButton(self, event):
        self.currentSSpath = config.animalImagesPath
        self.dataListEnglish = loadData.wildAnimalEnglish
        self.dataListNepali = loadData.wildAnimalNepali
        self.currentPosition = -1
        self.currentPosition = eUtils.nextSlide(self.currentPosition, len(self.dataListEnglish))
        self.displayText.SetLabel(self.dataListNepali[self.currentPosition])
        currentImg = join(self.currentSSpath, (self.dataListEnglish[self.currentPosition] + ".png"))
        self.displayImage.SetBitmap(wx.Bitmap(currentImg, wx.BITMAP_TYPE_PNG))
        self.displayType.SetLabel(messages.wildAnimal)
        
    def OnBirdButton(self, event):
        self.currentSSpath = config.birdImagesPath
        self.dataListEnglish = loadData.birdNameEnglish
        self.dataListNepali = loadData.birdNameNepali
        self.currentPosition = -1
        self.currentPosition = eUtils.nextSlide(self.currentPosition, len(self.dataListEnglish))
        self.displayText.SetLabel(self.dataListNepali[self.currentPosition])
        currentImg = join(self.currentSSpath, (self.dataListEnglish[self.currentPosition] + ".png"))
        self.displayImage.SetBitmap(wx.Bitmap(currentImg, wx.BITMAP_TYPE_PNG))
        self.displayType.SetLabel(messages.bird)

    def OnInsectButton(self, event):
        self.currentSSpath = config.insectImagesPath
        self.dataListEnglish = loadData.insectNameEnglish
        self.dataListNepali = loadData.insectNameNepali
        self.currentPosition = -1
        self.currentPosition = eUtils.nextSlide(self.currentPosition, len(self.dataListEnglish))
        self.displayText.SetLabel(self.dataListNepali[self.currentPosition])
        currentImg = join(self.currentSSpath, (self.dataListEnglish[self.currentPosition] + ".png"))
        self.displayImage.SetBitmap(wx.Bitmap(currentImg, wx.BITMAP_TYPE_PNG))
        self.displayType.SetLabel(messages.insect)
        
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
