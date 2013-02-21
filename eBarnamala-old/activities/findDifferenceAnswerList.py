import wx
import wx.lib.stattext as statTex
import random
import conf.config as config
import conf.messages as messages
from os.path import join

class charAnswerList():
    def __init__(self, parent, answer, questionList):
        if wx.Platform != "__WXGTK__":
            statText = wx.StaticText
        else:
            statText = statTex.GenStaticText
        self.buttonPressed = -1
        self.answer = answer
        self.fontSize = config.fontSize[4]
        self.eventQueue = []

        self.displayText1 = statText(parent, wx.ID_ANY, questionList[0], (100,25), style = wx.ALIGN_CENTRE)
        self.displayText1.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText1.SetBackgroundColour(config.backgroundColour)
        self.displayText1.Bind(wx.EVT_LEFT_DOWN, self.OnAns1, id=self.displayText1.GetId())

        self.displayText2 = statText(parent, wx.ID_ANY, questionList[1], (340,25), style = wx.ALIGN_CENTRE)
        self.displayText2.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText2.SetBackgroundColour(config.backgroundColour)
        self.displayText2.Bind(wx.EVT_LEFT_DOWN, self.OnAns2, id=self.displayText2.GetId())

        self.displayText3 = statText(parent, wx.ID_ANY, questionList[2], (560,25), style = wx.ALIGN_CENTRE)
        self.displayText3.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText3.SetBackgroundColour(config.backgroundColour)
        self.displayText3.Bind(wx.EVT_LEFT_DOWN, self.OnAns3, id=self.displayText3.GetId())

        self.displayText4 = statText(parent, wx.ID_ANY, questionList[3], (180,175), style = wx.ALIGN_CENTRE)
        self.displayText4.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText4.SetBackgroundColour(config.backgroundColour)
        self.displayText4.Bind(wx.EVT_LEFT_DOWN, self.OnAns4, id=self.displayText4.GetId())

        self.displayText5 = statText(parent, wx.ID_ANY, questionList[4], (440,175), style = wx.ALIGN_CENTRE)
        self.displayText5.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText5.SetBackgroundColour(config.backgroundColour)
        self.displayText5.Bind(wx.EVT_LEFT_DOWN, self.OnAns5, id=self.displayText5.GetId())

        self.problemMessage = statText(parent, wx.ID_ANY, messages.problemNoImageMessage, (320, 330), style = wx.ALIGN_CENTRE)
        self.problemMessage.SetFont(wx.Font(config.fontSize[1], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.problemMessage.SetBackgroundColour(config.backgroundColour)

        answerImg = wx.Bitmap(join(config.coreImagesPath, 'ansBlank.png'), wx.BITMAP_TYPE_PNG)
        self.answerImage = wx.StaticBitmap(parent, -1, answerImg, (100,330), (180,140))
        self.answerImage.SetBackgroundColour(config.backgroundColour)

    def nextQuestion(self, answer, questionList):
        if len(self.eventQueue) != 0:
            self.eventQueue[0].SetBackgroundColour(config.backgroundColour)
            self.eventQueue[0].SetLabel(self.eventQueue[0].GetLabel())
        self.eventQueue = []
        self.answer = answer
        self.answerImage.SetBitmap(wx.Bitmap(join(config.coreImagesPath, 'ansBlank.png'), wx.BITMAP_TYPE_PNG))
        self.displayText1.SetLabel(questionList[0])
        self.displayText2.SetLabel(questionList[1])
        self.displayText3.SetLabel(questionList[2])
        self.displayText4.SetLabel(questionList[3])
        self.displayText5.SetLabel(questionList[4])

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

    def OnAns4(self, event):
        self.eventQueue.append(event.GetEventObject())
        self.buttonPressed = 3
        self.changeBackgroundColour()
        answer = self.checkAnswer()
        self.displayResult(answer)

    def OnAns5(self, event):
        self.eventQueue.append(event.GetEventObject())
        self.buttonPressed = 4
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
        if self.answer == self.buttonPressed :
            answer = "Right"
        else:
            answer = "Wrong"
        return answer

    def displayResult(self, answer):
        if answer == "Right":
            self.answerImage.SetBitmap(wx.Bitmap(join(config.coreImagesPath, 'right.png'), wx.BITMAP_TYPE_PNG))
        else:
            self.answerImage.SetBitmap(wx.Bitmap(join(config.coreImagesPath, 'wrong.png'), wx.BITMAP_TYPE_PNG))
