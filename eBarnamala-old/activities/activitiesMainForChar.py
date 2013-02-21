import wx
import conf.config as config
import utils.bottomMenu as bottomMenu
import charMatch
import charImageMatch
import imageCharMatch
import numberFill
import countClick
import searchAndRecognize
import recognizeAndSearch
import findDifference
import matchPairs
from os.path import join

class activitiesMainPanel(wx.Panel):
    def __init__(self, parent, id, mainPanel, currentLesson):
        self.currentLesson = currentLesson
        self.charPosition = 0
        self.mainWin = mainPanel
        self.parent = parent
        self.imgInfo = [0,0]    #track img displayed. [0] for letter-img and [1] for within same letter
        self.blankImg = join(config.coreImagesPath, 'blank.png')
        buttonImages = []
        if self.currentLesson == "oneTwo":
            buttonImages.append('numberNumber.png')
            buttonImages.append('numberImage.png')
            buttonImages.append('imageNumber.png')
            buttonImages.append('numberFill.png')
            buttonImages.append('countClick.png')
            buttonImages.append('searchAndRecognize.png')
            buttonImages.append('')
            buttonImages.append('')
            buttonImages.append('')
            buttonImages.append('matchPairs.png')
        elif self.currentLesson == "kaKha":
            buttonImages.append('letterLetter.png')
            buttonImages.append('letterImage.png')
            buttonImages.append('imageLetter.png')
            buttonImages.append('')
            buttonImages.append('')
            buttonImages.append('searchAndRecognize.png')
            buttonImages.append('')
            buttonImages.append('findDifferenceChar.png')
            buttonImages.append('findDifference.png')
            buttonImages.append('matchPairs.png')
        elif self.currentLesson == "aaa":
            buttonImages.append('letterLetter.png')
            buttonImages.append('letterImage.png')
            buttonImages.append('imageLetter.png')
            buttonImages.append('')
            buttonImages.append('')
            buttonImages.append('searchAndRecognize.png')
            buttonImages.append('')
            buttonImages.append('findDifferenceChar.png')
            buttonImages.append('findDifference.png')
            buttonImages.append('matchPairs.png')
        elif self.currentLesson == "time":
            buttonImages.append('')
            buttonImages.append('timeImage.png')
            buttonImages.append('timeChar.png')
            buttonImages.append('')
            buttonImages.append('')
            buttonImages.append('searchAndRecognize.png')
            buttonImages.append('recognizeAndSearch.png')
            buttonImages.append('')
            buttonImages.append('')
            buttonImages.append('matchPairs.png')

        self.mainPanel = wx.Panel(parent, -1, (0, 0), (800, 600))
        self.mainPanel.SetBackgroundColour(config.backgroundColour)

        if buttonImages[0] != '':
            numberNumberImg = wx.Bitmap(join(config.buttonsPath, buttonImages[0]), wx.BITMAP_TYPE_PNG)
            self.numberNumberButton = wx.BitmapButton(self.mainPanel, 1, numberNumberImg, (40,100), style = wx.NO_BORDER)
            self.numberNumberButton.SetBackgroundColour(config.backgroundColour)
            self.numberNumberButton.Bind(wx.EVT_BUTTON, self.OnCharCharGame, id=1)
        else:
            pass

        if buttonImages[1] != '':
            numberImageImg = wx.Bitmap(join(config.buttonsPath, buttonImages[1]), wx.BITMAP_TYPE_PNG)
            self.numberImageButton = wx.BitmapButton(self.mainPanel, 2, numberImageImg, (300,100), style = wx.NO_BORDER)
            self.numberImageButton.SetBackgroundColour(config.backgroundColour)
            self.numberImageButton.Bind(wx.EVT_BUTTON, self.OnCharImageGame, id=2)
        else:
            pass

        if buttonImages[2] != '':
            imageNumberImg = wx.Bitmap(join(config.buttonsPath, buttonImages[2]), wx.BITMAP_TYPE_PNG)
            self.imageNumberButton = wx.BitmapButton(self.mainPanel, 3, imageNumberImg, (560,100), style = wx.NO_BORDER)
            self.imageNumberButton.SetBackgroundColour(config.backgroundColour)
            self.imageNumberButton.Bind(wx.EVT_BUTTON, self.OnImageCharGame, id=3)
        else:
            pass

        if buttonImages[3] != '':
            numberFillImg = wx.Bitmap(join(config.buttonsPath, buttonImages[3]), wx.BITMAP_TYPE_PNG)
            self.numberFillButton = wx.BitmapButton(self.mainPanel, 4, numberFillImg, (40,200), style = wx.NO_BORDER)
            self.numberFillButton.SetBackgroundColour(config.backgroundColour)
            self.numberFillButton.Bind(wx.EVT_BUTTON, self.OnNumberFillGame, id=4)
        else:
            pass

        if buttonImages[4] != '':
            countClickImg = wx.Bitmap(join(config.buttonsPath, buttonImages[4]), wx.BITMAP_TYPE_PNG)
            self.countClickButton = wx.BitmapButton(self.mainPanel, 5, countClickImg, (300,200), style = wx.NO_BORDER)
            self.countClickButton.SetBackgroundColour(config.backgroundColour)
            self.countClickButton.Bind(wx.EVT_BUTTON, self.OnCountClickGame, id=5)
        else:
            pass

        if buttonImages[5] != '':
            searchAndRecognizeImg = wx.Bitmap(join(config.buttonsPath, buttonImages[5]), wx.BITMAP_TYPE_PNG)
            self.searchAndRecognizeButton = wx.BitmapButton(self.mainPanel, 6, searchAndRecognizeImg, (560,200), style = wx.NO_BORDER)
            self.searchAndRecognizeButton.SetBackgroundColour(config.backgroundColour)
            self.searchAndRecognizeButton.Bind(wx.EVT_BUTTON, self.OnSearchAndRecognizeGame, id=6)
        else:
            pass

        if buttonImages[6] != '':
            recognizeAndSearchImg = wx.Bitmap(join(config.buttonsPath, buttonImages[6]), wx.BITMAP_TYPE_PNG)
            self.recognizeAndSearchButton = wx.BitmapButton(self.mainPanel, 7, recognizeAndSearchImg, (300,200), style = wx.NO_BORDER)
            self.recognizeAndSearchButton.SetBackgroundColour(config.backgroundColour)
            self.recognizeAndSearchButton.Bind(wx.EVT_BUTTON, self.OnRecognizeAndSearchGame, id=7)
        else:
            pass

        if buttonImages[7] != '':
            findDifferenceCharImg = wx.Bitmap(join(config.buttonsPath, buttonImages[7]), wx.BITMAP_TYPE_PNG)
            self.findDifferenceCharButton = wx.BitmapButton(self.mainPanel, 8, findDifferenceCharImg, (40,200), style = wx.NO_BORDER)
            self.findDifferenceCharButton.SetBackgroundColour(config.backgroundColour)
            self.findDifferenceCharButton.Bind(wx.EVT_BUTTON, self.OnFindDifferenceCharGame, id=8)
        else:
            pass

        if buttonImages[8] != '':
            findDifferenceImg = wx.Bitmap(join(config.buttonsPath, buttonImages[8]), wx.BITMAP_TYPE_PNG)
            self.findDifferenceButton = wx.BitmapButton(self.mainPanel, 9, findDifferenceImg, (300,200), style = wx.NO_BORDER)
            self.findDifferenceButton.SetBackgroundColour(config.backgroundColour)
            self.findDifferenceButton.Bind(wx.EVT_BUTTON, self.OnFindDifferenceGame, id=9)
        else:
            pass

        if buttonImages[9] != '':
            matchPairsImg = wx.Bitmap(join(config.buttonsPath, buttonImages[9]), wx.BITMAP_TYPE_PNG)
            self.matchPairsButton = wx.BitmapButton(self.mainPanel, 10, matchPairsImg, (40,300), style = wx.NO_BORDER)
            self.matchPairsButton.SetBackgroundColour(config.backgroundColour)
            self.matchPairsButton.Bind(wx.EVT_BUTTON, self.OnMatchPairsGame, id=10)
        else:
            pass

        bottomMenu.bottomMenu([self.mainPanel], parent, self.mainWin, 'twoButton')

    def OnCharCharGame(self, event):
        self.mainPanel.Show(False)
        self.mainWin.Show(False)
        charMatch.charMatch(self.parent, -1, self.mainWin, self.mainPanel, self.currentLesson)
        
    def OnCharImageGame(self, event):
        self.mainPanel.Show(False)
        self.mainWin.Show(False)
        charImageMatch.charImageMatch(self.parent, -1, self.mainWin, self.mainPanel, self.currentLesson)

    def OnImageCharGame(self, event):
        self.mainPanel.Show(False)
        self.mainWin.Show(False)
        imageCharMatch.imageCharMatch(self.parent, -1, self.mainWin, self.mainPanel, self.currentLesson)

    def OnNumberFillGame(self, event):
        self.mainPanel.Show(False)
        self.mainWin.Show(False)
        numberFill.numberFill(self.parent, -1, self.mainWin, self.mainPanel, self.currentLesson)

    def OnCountClickGame(self, event):
        self.mainPanel.Show(False)
        self.mainWin.Show(False)
        countClick.countClick(self.parent, -1, self.mainWin, self.mainPanel, self.currentLesson)

    def OnSearchAndRecognizeGame(self, event):
        self.mainPanel.Show(False)
        self.mainWin.Show(False)
        searchAndRecognize.searchAndRecognize(self.parent, -1, self.mainWin, self.mainPanel, self.currentLesson)

    def OnRecognizeAndSearchGame(self, event):
        self.mainPanel.Show(False)
        self.mainWin.Show(False)
        recognizeAndSearch.recognizeAndSearch(self.parent, -1, self.mainWin, self.mainPanel, self.currentLesson)

    def OnFindDifferenceCharGame(self, event):
        self.mainPanel.Show(False)
        self.mainWin.Show(False)
        findDifference.findDifference(self.parent, -1, self.mainWin, self.mainPanel, self.currentLesson, "Char")
        
    def OnFindDifferenceGame(self, event):
        self.mainPanel.Show(False)
        self.mainWin.Show(False)
        findDifference.findDifference(self.parent, -1, self.mainWin, self.mainPanel, self.currentLesson, "Img")

    def OnMatchPairsGame(self, event):
        self.mainPanel.Show(False)
        self.mainWin.Show(False)
        matchPairs.matchPairs(self.parent, -1, self.mainWin, self.mainPanel, self.currentLesson)
        
        
