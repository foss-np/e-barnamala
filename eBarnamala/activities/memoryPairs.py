import wx
import conf.config as config
import utils.wordActivitiesUtils as nGUtils
import utils.bottomMenu as bottomMenu
from os.path import join
import memoryImageCharAnswerList
import Image

class memoryPairs():
    def __init__(self, parent, id, mainWin, mainPanel, currentLesson):
        self.mainWin = mainWin
        self.mainPanel = mainPanel
        self.currentLesson = currentLesson
        
        self.questionList, self.questionImgList, self.answerList, self.answerNepaliList = nGUtils.nextMatchImageCharQuestion(self.currentLesson)
        
        self.displayPanel = wx.Panel(parent, -1, (0, 0), (800, 600))
        self.displayPanel.SetBackgroundColour(config.backgroundColour)

        self.memoryImageCharAnswerList = memoryImageCharAnswerList.memoryImageCharAnswerList(self.displayPanel, self.questionList, self.questionImgList, self.answerList, self.answerNepaliList, self.currentLesson)

        nextQuestionImg = wx.Bitmap(join(config.buttonsPath,'nextQuestion.png'), wx.BITMAP_TYPE_PNG)
        self.nextQuestionButton = wx.BitmapButton(self.displayPanel, 4, nextQuestionImg, (460,400), style = wx.NO_BORDER)
        self.nextQuestionButton.SetBackgroundColour(config.backgroundColour)
        self.nextQuestionButton.Bind(wx.EVT_BUTTON, self.OnNextQuestion, id=4)

        bottomMenu.bottomMenu([self.displayPanel], parent, self.mainWin, 'threeButton', self.mainPanel)
        
    def OnNextQuestion(self, event=None):
        self.questionList, self.questionImgList, self.answerList, self.answerNepaliList = nGUtils.nextMatchImageCharQuestion(self.currentLesson)
        self.memoryImageCharAnswerList.nextQuestion(self.questionList, self.questionImgList, self.answerList, self.answerNepaliList)
