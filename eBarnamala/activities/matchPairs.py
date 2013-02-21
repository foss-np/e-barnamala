import wx
import conf.config as config
import utils.wordActivitiesUtils as nGUtils
import utils.bottomMenu as bottomMenu
from os.path import join
import matchImageCharAnswerList
import Image

class matchPairs():
    def __init__(self, parent, id, mainWin, mainPanel, currentLesson):
        self.mainWin = mainWin
        self.mainPanel = mainPanel
        self.currentLesson = currentLesson
        
        self.questionList, self.questionImgList, self.answerList, self.answerNepaliList = nGUtils.nextMatchImageCharQuestion(self.currentLesson)
        self.questionImgList = resizeImage(self.questionImgList, 50)
        
        self.displayPanel = wx.Panel(parent, -1, (0, 0), (800, 600))
        self.displayPanel.SetBackgroundColour(config.backgroundColour)

        self.matchImageCharAnswerList = matchImageCharAnswerList.matchImageCharAnswerList(self.displayPanel, self.questionList, self.questionImgList, self.answerList, self.answerNepaliList, self.currentLesson)

        nextQuestionImg = wx.Bitmap(join(config.buttonsPath,'nextQuestion.png'), wx.BITMAP_TYPE_PNG)
        self.nextQuestionButton = wx.BitmapButton(self.displayPanel, 4, nextQuestionImg, (460,400), style = wx.NO_BORDER)
        self.nextQuestionButton.SetBackgroundColour(config.backgroundColour)
        self.nextQuestionButton.Bind(wx.EVT_BUTTON, self.OnNextQuestion, id=4)

        bottomMenu.bottomMenu([self.displayPanel], parent, self.mainWin, 'threeButton', self.mainPanel)
        
    def OnNextQuestion(self, event=None):
        self.questionList, self.questionImgList, self.answerList, self.answerNepaliList = nGUtils.nextMatchImageCharQuestion(self.currentLesson)
        self.questionImgList = resizeImage(self.questionImgList, 50)
        self.matchImageCharAnswerList.nextQuestion(self.questionList, self.questionImgList, self.answerList, self.answerNepaliList)
        
def resizeImage(imageList, resizePercent):
    newImageList = []
    for i in imageList:
        temp = Image.open(i)
        temp = temp.resize(((resizePercent*temp.size[0])/100,(resizePercent*temp.size[1])/100), Image.ANTIALIAS)
        returnNumberImg = wx.EmptyImage(temp.size[0], temp.size[1])
        returnNumberImg.SetData(temp.convert('RGB').tostring())
        returnNumberImg.SetAlphaData(temp.convert("RGBA").tostring()[3::4])
        newImageList.append(returnNumberImg)
    return newImageList

