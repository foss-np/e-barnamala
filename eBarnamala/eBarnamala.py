#!/usr/bin/python

import wx
import utils.eUtils as eUtils
import conf.config as config
import lessons.learnLetters as learnLetters
import lessons.learnTime as learnTime
import lessons.learnTrafficSign as learnTrafficSign
import lessons.learnAnimals as learnAnimals
import lessons.learnColours as learnColours
import lessons.learnMoney as learnMoney
import lessons.learnArithmetic as learnArithmetic
import activities.activitiesMainForChar as activitiesMainForChar
import activities.activitiesMainForWords as activitiesMainForWords
import utils.bottomMenu as bottomMenu
from os.path import join

class mainApp(wx.App):
    """
    main class for eBarnamala. Sets up the initial screen with the buttons arranged for lessons and activities
    The opened window is fixed at 800,600 resolution. Also uses absolute positioning. 
    Need to change to sizers later on.
    Cursor is changed to custom for windows.
    currentLesson variable is also set in its functions. 
    """
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        
        self.mainFrame = wx.Frame(None, wx.ID_ANY, title = u'\u0908 \u092C\u0930\u094D\u0923\u092E\u093E\u0932\u093E', pos =(0, 0), size = (800, 600))
        self.mainFrame.SetIcon(wx.Icon(join(config.iconsPath,'eBarnamalaIcon.ico'), wx.BITMAP_TYPE_ICO))
        self.mainFrame.SetBackgroundColour(config.backgroundColour)

        if wx.Platform != "__WXGTK__":
            cursorImg = wx.Bitmap(join(config.cursorPath, 'basicArrow.png'), wx.BITMAP_TYPE_PNG)
            cursorImg = cursorImg.ConvertToImage()
            cursorImg.ConvertAlphaToMask(220)
            cursor = wx.CursorFromImage(cursorImg)
            self.mainFrame.SetCursor(cursor)
        else:
            cursor = wx.StockCursor(wx.CURSOR_ARROW)
            self.mainFrame.SetCursor(cursor)
        
        self.mainPanel = wx.Panel(self.mainFrame, wx.ID_ANY, (0, 0), (800, 600))
        self.mainPanel.SetBackgroundColour(config.backgroundColour)
        
        learnLettersImg = wx.Bitmap(join(config.buttonsPath,'learnLetters.png'), wx.BITMAP_TYPE_PNG)
        self.learnLettersButton = wx.BitmapButton(self.mainPanel, wx.ID_ANY, learnLettersImg, (40,368), style = wx.NO_BORDER)
        self.learnLettersButton.SetBackgroundColour(config.backgroundColour)
        self.learnLettersButton.Bind(wx.EVT_BUTTON, self.OnLearnLetters, id=self.learnLettersButton.GetId())

        learnTimeImg = wx.Bitmap(join(config.buttonsPath,'learnTime.png'), wx.BITMAP_TYPE_PNG)
        self.learnTimeButton = wx.BitmapButton(self.mainPanel, wx.ID_ANY, learnTimeImg, (40,316), style = wx.NO_BORDER)
        self.learnTimeButton.SetBackgroundColour(config.backgroundColour)
        self.learnTimeButton.Bind(wx.EVT_BUTTON, self.OnLearnTime, id=self.learnTimeButton.GetId())

        learnAnimalsImg = wx.Bitmap(join(config.buttonsPath,'learnAnimals.png'), wx.BITMAP_TYPE_PNG)
        self.learnAnimalsButton = wx.BitmapButton(self.mainPanel, wx.ID_ANY, learnAnimalsImg, (40,264), style = wx.NO_BORDER)
        self.learnAnimalsButton.SetBackgroundColour(config.backgroundColour)
        self.learnAnimalsButton.Bind(wx.EVT_BUTTON, self.OnLearnAnimals, id=self.learnAnimalsButton.GetId())

        learnTrafficSignsImg = wx.Bitmap(join(config.buttonsPath,'trafficSigns.png'), wx.BITMAP_TYPE_PNG)
        self.learnTrafficSignsButton = wx.BitmapButton(self.mainPanel, wx.ID_ANY, learnTrafficSignsImg, (40,212), style = wx.NO_BORDER)
        self.learnTrafficSignsButton.SetBackgroundColour(config.backgroundColour)
        self.learnTrafficSignsButton.Bind(wx.EVT_BUTTON, self.OnLearnTrafficSigns, id=self.learnTrafficSignsButton.GetId())

        learnColoursImg = wx.Bitmap(join(config.buttonsPath,'colours.png'), wx.BITMAP_TYPE_PNG)
        self.learnColoursButton = wx.BitmapButton(self.mainPanel, wx.ID_ANY, learnColoursImg, (40,160), style = wx.NO_BORDER)
        self.learnColoursButton.SetBackgroundColour(config.backgroundColour)
        self.learnColoursButton.Bind(wx.EVT_BUTTON, self.OnLearnColours, id=self.learnColoursButton.GetId())

        learnMoneyImg = wx.Bitmap(join(config.buttonsPath,'learnMoney.png'), wx.BITMAP_TYPE_PNG)
        self.learnMoneyButton = wx.BitmapButton(self.mainPanel, wx.ID_ANY, learnMoneyImg, (40,110), style = wx.NO_BORDER)
        self.learnMoneyButton.SetBackgroundColour(config.backgroundColour)
        self.learnMoneyButton.Bind(wx.EVT_BUTTON, self.OnLearnMoney, id=self.learnMoneyButton.GetId())

        arithmeticImg = wx.Bitmap(join(config.buttonsPath,'arithmetic.png'), wx.BITMAP_TYPE_PNG)
        self.arithmeticButton = wx.BitmapButton(self.mainPanel, wx.ID_ANY, arithmeticImg, (40,60), style = wx.NO_BORDER)
        self.arithmeticButton.SetBackgroundColour(config.backgroundColour)
        self.arithmeticButton.Bind(wx.EVT_BUTTON, self.OnLearnArithmetic, id=self.arithmeticButton.GetId())

        numberActivitiesImg = wx.Bitmap(join(config.buttonsPath,'playNumbers.png'), wx.BITMAP_TYPE_PNG)
        self.numberActivitiesButton = wx.BitmapButton(self.mainPanel, wx.ID_ANY, numberActivitiesImg, (220,368), style = wx.NO_BORDER)
        self.numberActivitiesButton.SetBackgroundColour(config.backgroundColour)
        self.numberActivitiesButton.Bind(wx.EVT_BUTTON, self.OnNumberActivities, id=self.numberActivitiesButton.GetId())

        sworActivitiesImg = wx.Bitmap(join(config.buttonsPath,'playSwor.png'), wx.BITMAP_TYPE_PNG)
        self.sworActivitiesButton = wx.BitmapButton(self.mainPanel, wx.ID_ANY, sworActivitiesImg, (220,316), style = wx.NO_BORDER)
        self.sworActivitiesButton.SetBackgroundColour(config.backgroundColour)
        self.sworActivitiesButton.Bind(wx.EVT_BUTTON, self.OnSworActivities, id=self.sworActivitiesButton.GetId())

        byanjanActivitiesImg = wx.Bitmap(join(config.buttonsPath,'playByanjan.png'), wx.BITMAP_TYPE_PNG)
        self.byanjanActivitiesButton = wx.BitmapButton(self.mainPanel, wx.ID_ANY, byanjanActivitiesImg, (220,264), style = wx.NO_BORDER)
        self.byanjanActivitiesButton.SetBackgroundColour(config.backgroundColour)
        self.byanjanActivitiesButton.Bind(wx.EVT_BUTTON, self.OnByanjanActivities, id=self.byanjanActivitiesButton.GetId())

        timeActivitiesImg = wx.Bitmap(join(config.buttonsPath,'time.png'), wx.BITMAP_TYPE_PNG)
        self.timeActivitiesButton = wx.BitmapButton(self.mainPanel, wx.ID_ANY, timeActivitiesImg, (220,212), style = wx.NO_BORDER)
        self.timeActivitiesButton.SetBackgroundColour(config.backgroundColour)
        self.timeActivitiesButton.Bind(wx.EVT_BUTTON, self.OnTimeActivities, id=self.timeActivitiesButton.GetId())

        colourActivitiesImg = wx.Bitmap(join(config.buttonsPath,'playColours.png'), wx.BITMAP_TYPE_PNG)
        self.colourActivitiesButton = wx.BitmapButton(self.mainPanel, wx.ID_ANY, colourActivitiesImg, (220,160), style = wx.NO_BORDER)
        self.colourActivitiesButton.SetBackgroundColour(config.backgroundColour)
        self.colourActivitiesButton.Bind(wx.EVT_BUTTON, self.OnColourActivities, id=self.colourActivitiesButton.GetId())

        animalActivitiesImg = wx.Bitmap(join(config.buttonsPath,'playAnimals.png'), wx.BITMAP_TYPE_PNG)
        self.animalActivitiesButton = wx.BitmapButton(self.mainPanel, wx.ID_ANY, animalActivitiesImg, (220,110), style = wx.NO_BORDER)
        self.animalActivitiesButton.SetBackgroundColour(config.backgroundColour)
        self.animalActivitiesButton.Bind(wx.EVT_BUTTON, self.OnAnimalActivities, id=self.animalActivitiesButton.GetId())

        splashImg = wx.Bitmap(config.splashImage, wx.BITMAP_TYPE_PNG)
        self.splashImage = wx.StaticBitmap(self.mainPanel, wx.ID_ANY, splashImg, (420,110), (splashImg.GetWidth(), splashImg.GetHeight()))

        bottomMenu.bottomMenu([self.mainPanel], self.mainFrame, self.mainPanel, 'oneButton')

        self.mainFrame.Show(True)

    def OnLearnLetters(self, event):
        self.mainPanel.Show(False)
        learnLetters.learnLettersPanel(self.mainFrame, wx.ID_ANY, self.mainPanel)

    def OnLearnTime(self, event):
        self.mainPanel.Show(False)
        learnTime.learnTimePanel(self.mainFrame, wx.ID_ANY, self.mainPanel)

    def OnLearnColours(self, event):
        self.mainPanel.Show(False)
        learnColours.learnColoursPanel(self.mainFrame, wx.ID_ANY, self.mainPanel)

    def OnLearnAnimals(self, event):
        self.mainPanel.Show(False)
        learnAnimals.learnAnimalsPanel(self.mainFrame, wx.ID_ANY, self.mainPanel)

    def OnLearnMoney(self, event):
        self.mainPanel.Show(False)
        learnMoney.learnMoneyPanel(self.mainFrame, wx.ID_ANY, self.mainPanel)

    def OnLearnTrafficSigns(self, event):
        self.mainPanel.Show(False)
        learnTrafficSign.learnTrafficSignPanel(self.mainFrame, wx.ID_ANY, self.mainPanel)

    def OnLearnArithmetic(self, event):
        self.mainPanel.Show(False)
        learnArithmetic.learnArithmeticPanel(self.mainFrame, wx.ID_ANY, self.mainPanel)

    def OnNumberActivities(self, event):
        currentLesson = "oneTwo"
        self.mainPanel.Show(False)
        activitiesMainForChar.activitiesMainPanel(self.mainFrame, wx.ID_ANY, self.mainPanel, currentLesson)

    def OnSworActivities(self, event):
        currentLesson = "aaa"
        self.mainPanel.Show(False)
        activitiesMainForChar.activitiesMainPanel(self.mainFrame, wx.ID_ANY, self.mainPanel, currentLesson)

    def OnByanjanActivities(self, event):
        currentLesson = "kaKha"
        self.mainPanel.Show(False)
        activitiesMainForChar.activitiesMainPanel(self.mainFrame, wx.ID_ANY, self.mainPanel, currentLesson)

    def OnTimeActivities(self, event):
        currentLesson = "time"
        self.mainPanel.Show(False)
        activitiesMainForChar.activitiesMainPanel(self.mainFrame, wx.ID_ANY, self.mainPanel, currentLesson)

    def OnColourActivities(self, event):
        currentLesson = "colour"
        self.mainPanel.Show(False)
        activitiesMainForWords.activitiesMainPanel(self.mainFrame, wx.ID_ANY, self.mainPanel, currentLesson)

    def OnAnimalActivities(self, event):
        currentLesson = "animals"
        self.mainPanel.Show(False)
        activitiesMainForWords.activitiesMainPanel(self.mainFrame, wx.ID_ANY, self.mainPanel, currentLesson)

if __name__ == '__main__':
    try:
        import psyco
        psyco.profile()
    except ImportError:
        pass

    app = mainApp()
    app.MainLoop()
