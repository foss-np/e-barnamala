import wx
import wx.lib.stattext as statTex
import conf.config as config
import utils.charActivitiesUtils as nGUtils
import utils.bottomMenu as bottomMenu
from os.path import join

class imageCharMatch(wx.Panel):
    def __init__(self, parent, id, mainWin, mainPanel, currentLesson):
        if wx.Platform != "__WXGTK__":
            statText = wx.StaticText
        else:
            statText = statTex.GenStaticText
        self.mainWin = mainWin
        self.mainPanel = mainPanel
        self.currentLesson = currentLesson
        self.buttonPressed = 20
        self.question = ''
        self.eventQueue = []

        self.question, self.answerList, self.answerImageList = nGUtils.nextImageMatchQuestion(self.currentLesson)
        self.checkNumberSet()

        self.fontSize = config.fontSize[4]
        if currentLesson == 'aaa': self.fontSize = config.fontSize[4]
        if currentLesson == 'kaKha': self.fontSize = config.fontSize[4]
        if currentLesson == 'oneTwo': self.fontSize = config.fontSize[5]
        if currentLesson == 'time': self.fontSize = config.fontSize[4]

        self.displayPanel = wx.Panel(parent, -1, (0, 0), (800, 600))
        self.displayPanel.SetBackgroundColour(config.backgroundColour)

        questionImg = wx.Bitmap(self.answerImageList[self.answerList.index(self.question)], wx.BITMAP_TYPE_PNG)
        self.questionImage = wx.StaticBitmap(self.displayPanel, 1, questionImg, (40,80), (questionImg.GetWidth(), questionImg.GetHeight()))

        displayImg = wx.Bitmap(join(config.coreImagesPath, 'divider.png'), wx.BITMAP_TYPE_PNG)
        self.displayImage = wx.StaticBitmap(self.displayPanel, -1, displayImg, (240,80), (displayImg.GetWidth(), displayImg.GetHeight()))

        self.displayText1 = statText(self.displayPanel, 1, self.answerList[0], (280, 70), style = wx.ALIGN_CENTRE)
        self.displayText1.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText1.SetBackgroundColour(config.backgroundColour)
        self.displayText1.Bind(wx.EVT_LEFT_DOWN, self.OnAns1, id=1)

        self.displayText2 = statText(self.displayPanel, 2, self.answerList[1], (440, 70), style = wx.ALIGN_CENTRE)
        self.displayText2.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText2.SetBackgroundColour(config.backgroundColour)
        self.displayText2.Bind(wx.EVT_LEFT_DOWN, self.OnAns2, id=2)

        self.displayText3 = statText(self.displayPanel, 3, self.answerList[2], (620, 70), style = wx.ALIGN_CENTRE)
        self.displayText3.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText3.SetBackgroundColour(config.backgroundColour)
        self.displayText3.Bind(wx.EVT_LEFT_DOWN, self.OnAns3, id=3)

        answerImg = wx.Bitmap(join(config.coreImagesPath, 'ansBlank.png'), wx.BITMAP_TYPE_PNG)
        self.answerImage = wx.StaticBitmap(self.displayPanel, -1, answerImg, (160,300), (180,140))
        self.answerImage.SetBackgroundColour(config.backgroundColour)

        nextQuestionImg = wx.Bitmap(join(config.buttonsPath,'nextQuestion.png'), wx.BITMAP_TYPE_PNG)
        self.nextQuestionButton = wx.BitmapButton(self.displayPanel, 4, nextQuestionImg, (460,320), style = wx.NO_BORDER)
        self.nextQuestionButton.SetBackgroundColour(config.backgroundColour)
        self.nextQuestionButton.Bind(wx.EVT_BUTTON, self.OnNextQuestion, id=4)

        bottomMenu.bottomMenu([self.displayPanel], parent, self.mainWin, 'threeButton', self.mainPanel)
        
    def OnNextQuestion(self, event=None):
        if len(self.eventQueue) != 0:
            self.eventQueue[0].SetBackgroundColour(config.backgroundColour)
            self.eventQueue[0].SetLabel(self.eventQueue[0].GetLabel())
        self.eventQueue = []
        self.answerImage.SetBitmap(wx.Bitmap(join(config.coreImagesPath, 'ansBlank.png'), wx.BITMAP_TYPE_PNG))
        self.questionImage.SetBitmap(wx.Bitmap(join(config.coreImagesPath, 'blank.png'), wx.BITMAP_TYPE_PNG))
        self.question, self.answerList, self.answerImageList = nGUtils.nextImageMatchQuestion(self.currentLesson)
        self.questionImage.SetBitmap(wx.Bitmap(self.answerImageList[self.answerList.index(self.question)], wx.BITMAP_TYPE_PNG))
        self.checkNumberSet()
        self.displayText1.SetLabel(self.answerList[0])
        self.displayText2.SetLabel(self.answerList[1])
        self.displayText3.SetLabel(self.answerList[2])

    def OnAns1(self, event):
        self.eventQueue.append(event.GetEventObject())
        self.buttonPressed = 0
        self.changeBackgroundColour()
        answer = self.checkAnswer()
        self.displayResult(answer)

    def OnAns2(self, event):
        self.eventQueue.append(event.GetEventObject())
        self.buttonPressed = 1
        self.changeBackgroundColour()
        answer = self.checkAnswer()
        self.displayResult(answer)

    def OnAns3(self, event):
        self.eventQueue.append(event.GetEventObject())
        self.buttonPressed = 2
        self.changeBackgroundColour()
        answer = self.checkAnswer()
        self.displayResult(answer)

    def changeBackgroundColour(self):
        if len(self.eventQueue) == 1:
            self.eventQueue[0].SetBackgroundColour(config.fillColour)
            self.eventQueue[0].SetLabel(self.eventQueue[0].GetLabel())
        elif len(self.eventQueue) == 2:
            self.eventQueue[0].SetBackgroundColour(config.backgroundColour)
            self.eventQueue[0].SetLabel(self.eventQueue[0].GetLabel())
            self.eventQueue.pop(0)
            self.eventQueue[0].SetBackgroundColour(config.fillColour)
            self.eventQueue[0].SetLabel(self.eventQueue[0].GetLabel())

    def checkAnswer(self):
        answer = ''
        if self.question == self.answerList[self.buttonPressed]:
            answer = "Right"
        else:
            answer = "Wrong"
        return answer

    def displayResult(self, answer):
        if answer == "Right":
            self.answerImage.SetBitmap(wx.Bitmap(join(config.coreImagesPath, 'right.png'), wx.BITMAP_TYPE_PNG))
        else:
            self.answerImage.SetBitmap(wx.Bitmap(join(config.coreImagesPath, 'wrong.png'), wx.BITMAP_TYPE_PNG))
            
##  This function is to check for double printing of chars like && in Linux.
##  The function is kept here to solve problems occuring only in specific modules like this one.
    def checkNumberSet(self):
        if wx.Platform == "__WXGTK__":
            for i in range(len(self.answerList)):
                if self.answerList[i] == '&&':
                    self.answerList[i] = self.answerList[i][0]
        else:
            pass
