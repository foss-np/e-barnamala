import wx
import conf.config as config
import utils.bottomMenu as bottomMenu
import recognizeAndSearch
import searchAndRecognize
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
        if self.currentLesson == "colour":
            buttonImages.append('recognizeAndSearch.png')
            buttonImages.append('searchAndRecognize.png')
            buttonImages.append('findDifference.png')
            buttonImages.append('matchPairs.png')
        if self.currentLesson == "animals":
            buttonImages.append('recognizeAndSearch.png')
            buttonImages.append('searchAndRecognize.png')
            buttonImages.append('findDifference.png')
            buttonImages.append('matchPairs.png')
        
        self.mainPanel = wx.Panel(parent, -1, (0, 0), (800, 600))
        self.mainPanel.SetBackgroundColour(config.backgroundColour)

        if buttonImages[0] != '':
            recAndSearchImg = wx.Bitmap(join(config.buttonsPath, buttonImages[0]), wx.BITMAP_TYPE_PNG)
            self.recAndSearchButton = wx.BitmapButton(self.mainPanel, wx.ID_ANY, recAndSearchImg, (40,100), style = wx.NO_BORDER)
            self.recAndSearchButton.SetBackgroundColour(config.backgroundColour)
            self.recAndSearchButton.Bind(wx.EVT_BUTTON, self.OnRecAndSearchGame, id=self.recAndSearchButton.GetId())
        else:
            pass

        if buttonImages[1] != '':
            searchAndRecImg = wx.Bitmap(join(config.buttonsPath, buttonImages[1]), wx.BITMAP_TYPE_PNG)
            self.searchAndRecButton = wx.BitmapButton(self.mainPanel, wx.ID_ANY, searchAndRecImg, (300,100), style = wx.NO_BORDER)
            self.searchAndRecButton.SetBackgroundColour(config.backgroundColour)
            self.searchAndRecButton.Bind(wx.EVT_BUTTON, self.OnSearchAndRecGame, id=self.searchAndRecButton.GetId())
        else:
            pass

        if buttonImages[2] != '':
            findDifferenceImg = wx.Bitmap(join(config.buttonsPath, buttonImages[2]), wx.BITMAP_TYPE_PNG)
            self.findDifferenceButton = wx.BitmapButton(self.mainPanel, wx.ID_ANY, findDifferenceImg, (550,100), style = wx.NO_BORDER)
            self.findDifferenceButton.SetBackgroundColour(config.backgroundColour)
            self.findDifferenceButton.Bind(wx.EVT_BUTTON, self.OnFindDifferenceGame, id=self.findDifferenceButton.GetId())
        else:
            pass

        if buttonImages[3] != '':
            matchPairsImg = wx.Bitmap(join(config.buttonsPath, buttonImages[3]), wx.BITMAP_TYPE_PNG)
            self.matchPairsButton = wx.BitmapButton(self.mainPanel, wx.ID_ANY, matchPairsImg, (40,200), style = wx.NO_BORDER)
            self.matchPairsButton.SetBackgroundColour(config.backgroundColour)
            self.matchPairsButton.Bind(wx.EVT_BUTTON, self.OnMatchPairsGame, id=self.matchPairsButton.GetId())
        else:
            pass

        bottomMenu.bottomMenu([self.mainPanel], parent, self.mainWin, 'twoButton')

    def OnRecAndSearchGame(self, event):
        self.mainPanel.Show(False)
        self.mainWin.Show(False)
        recognizeAndSearch.recognizeAndSearch(self.parent, -1, self.mainWin, self.mainPanel, self.currentLesson)

    def OnSearchAndRecGame(self, event):
        self.mainPanel.Show(False)
        self.mainWin.Show(False)
        searchAndRecognize.searchAndRecognize(self.parent, -1, self.mainWin, self.mainPanel, self.currentLesson)

    def OnFindDifferenceGame(self, event):
        self.mainPanel.Show(False)
        self.mainWin.Show(False)
        findDifference.findDifference(self.parent, -1, self.mainWin, self.mainPanel, self.currentLesson, "Img")

    def OnMatchPairsGame(self, event):
        self.mainPanel.Show(False)
        self.mainWin.Show(False)
        matchPairs.matchPairs(self.parent, -1, self.mainWin, self.mainPanel, self.currentLesson)
