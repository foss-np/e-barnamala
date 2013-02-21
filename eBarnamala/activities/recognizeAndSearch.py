import wx
import conf.config as config
import utils.wordActivitiesUtils as nGUtils
import utils.bottomMenu as bottomMenu
from os.path import join
import wordAnswerList
import Image

class recognizeAndSearch():
    def __init__(self, parent, id, mainWin, mainPanel, currentLesson):
        self.mainWin = mainWin
        self.mainPanel = mainPanel
        self.currentLesson = currentLesson
        self.question = ''
        self.fontSize = config.fontSize[5]
        
        self.question, self.questionImg, self.answerList = nGUtils.nextRecognizeAndSearchQuestion(self.currentLesson)
        
        self.displayPanel = wx.Panel(parent, -1, (0, 0), (800, 600))
        self.displayPanel.SetBackgroundColour(config.backgroundColour)

        questionImg = wx.Bitmap(self.questionImg, wx.BITMAP_TYPE_PNG)
        self.questionImage = wx.StaticBitmap(self.displayPanel, wx.ID_ANY, questionImg, (280,30), (questionImg.GetWidth(), questionImg.GetHeight()))
        self.questionImage.SetBackgroundColour(config.backgroundColour)
        
        self.wordAnswerList = wordAnswerList.wordAnswerList(self.displayPanel, self.question, self.answerList, self.currentLesson)

        nextQuestionImg = wx.Bitmap(join(config.buttonsPath,'nextQuestion.png'), wx.BITMAP_TYPE_PNG)
        self.nextQuestionButton = wx.BitmapButton(self.displayPanel, 4, nextQuestionImg, (460,400), style = wx.NO_BORDER)
        self.nextQuestionButton.SetBackgroundColour(config.backgroundColour)
        self.nextQuestionButton.Bind(wx.EVT_BUTTON, self.OnNextQuestion, id=4)

        bottomMenu.bottomMenu([self.displayPanel], parent, self.mainWin, 'threeButton', self.mainPanel)
        
    def OnNextQuestion(self, event=None):
        self.question, self.questionImg, self.answerList = nGUtils.nextRecognizeAndSearchQuestion(self.currentLesson)
        self.questionImage.SetBitmap(wx.Bitmap(self.questionImg, wx.BITMAP_TYPE_PNG))
        self.wordAnswerList.nextQuestion(self.question, self.answerList)
