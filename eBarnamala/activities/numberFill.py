import wx
import conf.config as config
import utils.charActivitiesUtils as nGUtils
import utils.bottomMenu as bottomMenu
from os.path import join
import numberAnswerList

class numberFill():
    def __init__(self, parent, id, mainWin, mainPanel, currentLesson):
        self.mainWin = mainWin
        self.mainPanel = mainPanel
        self.currentLesson = currentLesson
        self.buttonPressed = 20
        self.question = ''
        self.fontSize = config.fontSize[5]
        temp = 0
        
        self.question, self.answerList, self.totalList = nGUtils.nextCharFillQuestion(self.currentLesson)

        if currentLesson == 'aaa': self.fontSize = config.fontSize[4]
        if currentLesson == 'kaKha': self.fontSize = config.fontSize[4]
        if currentLesson == 'oneTwo': self.fontSize = config.fontSize[5]

        self.displayPanel = wx.Panel(parent, -1, (0, 0), (800, 600))
        self.displayPanel.SetBackgroundColour(config.backgroundColour)

        temp = self.answerList.index(self.question)
        self.answerList[temp] = u'\u00A4'

        self.displayText1 = wx.StaticText(self.displayPanel, 1, self.answerList[0], (120, 40), style = wx.ALIGN_CENTRE)
        self.displayText1.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText1.SetBackgroundColour(config.backgroundColour)
        
        self.displayText2 = wx.StaticText(self.displayPanel, 2, self.answerList[1], (280, 40), style = wx.ALIGN_CENTRE)
        self.displayText2.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText2.SetBackgroundColour(config.backgroundColour)
        
        self.displayText3 = wx.StaticText(self.displayPanel, 3, self.answerList[2], (440, 40), style = wx.ALIGN_CENTRE)
        self.displayText3.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText3.SetBackgroundColour(config.backgroundColour)

        self.numberAnswerList = numberAnswerList.numberAnswerList(self.displayPanel, self.question, self.totalList)

        nextQuestionImg = wx.Bitmap(join(config.buttonsPath,'nextQuestion.png'), wx.BITMAP_TYPE_PNG)
        self.nextQuestionButton = wx.BitmapButton(self.displayPanel, 4, nextQuestionImg, (460,400), style = wx.NO_BORDER)
        self.nextQuestionButton.SetBackgroundColour(config.backgroundColour)
        self.nextQuestionButton.Bind(wx.EVT_BUTTON, self.OnNextQuestion, id=4)

        bottomMenu.bottomMenu([self.displayPanel], parent, self.mainWin, 'threeButton', self.mainPanel)
        
    def OnNextQuestion(self, event=None):
        temp = 0
        self.question, self.answerList, self.totalList = nGUtils.nextCharFillQuestion(self.currentLesson)
        temp = self.answerList.index(self.question)
        self.answerList[temp] = u'\u00A4'
        self.numberAnswerList.nextQuestion(self.question, self.totalList)
        self.displayText1.SetLabel(self.answerList[0])
        self.displayText2.SetLabel(self.answerList[1])
        self.displayText3.SetLabel(self.answerList[2])
                              
