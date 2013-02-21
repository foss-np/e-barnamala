import wx
import wx.lib.statbmp as statbp
import random
import conf.config as config
import conf.messages as messages
from os.path import join

class imageAnswerList():
    def __init__(self, parent, answer, questionImgList):
        if wx.Platform != "__WXGTK__":
            statbmp = wx.StaticBitmap
        else:
            statbmp = statbp.GenStaticBitmap
        self.buttonPressed = -1
        self.answer = answer
        self.fontSize = config.fontSize[1]
        self.eventQueue = []

        questionImg0 = wx.BitmapFromImage(questionImgList[0])
        self.questionImage0 = statbmp(parent, wx.ID_ANY, questionImg0, (100,25), (questionImg0.GetWidth(), questionImg0.GetHeight()))
        self.questionImage0.SetBackgroundColour(config.backgroundColour)
        self.questionImage0.Bind(wx.EVT_LEFT_DOWN, self.OnAns1, id=self.questionImage0.GetId())
        
        questionImg1 = wx.BitmapFromImage(questionImgList[1])
        self.questionImage1 = statbmp(parent, wx.ID_ANY, questionImg1, (340,25), (questionImg1.GetWidth(), questionImg1.GetHeight()))
        self.questionImage1.SetBackgroundColour(config.backgroundColour)
        self.questionImage1.Bind(wx.EVT_LEFT_DOWN, self.OnAns2, id=self.questionImage1.GetId())

        questionImg2 = wx.BitmapFromImage(questionImgList[2])
        self.questionImage2 = statbmp(parent, wx.ID_ANY, questionImg2, (560,25), (questionImg2.GetWidth(), questionImg2.GetHeight()))
        self.questionImage2.SetBackgroundColour(config.backgroundColour)
        self.questionImage2.Bind(wx.EVT_LEFT_DOWN, self.OnAns3, id=self.questionImage2.GetId())

        questionImg3 = wx.BitmapFromImage(questionImgList[3])
        self.questionImage3 = statbmp(parent, wx.ID_ANY, questionImg3, (180,175), (questionImg3.GetWidth(), questionImg3.GetHeight()))
        self.questionImage3.SetBackgroundColour(config.backgroundColour)
        self.questionImage3.Bind(wx.EVT_LEFT_DOWN, self.OnAns4, id=self.questionImage3.GetId())

        questionImg4 = wx.BitmapFromImage(questionImgList[4])
        self.questionImage4 = statbmp(parent, wx.ID_ANY, questionImg4, (440,175), (questionImg4.GetWidth(), questionImg4.GetHeight()))
        self.questionImage4.SetBackgroundColour(config.backgroundColour)
        self.questionImage4.Bind(wx.EVT_LEFT_DOWN, self.OnAns5, id=self.questionImage4.GetId())

        self.problemMessage = wx.StaticText(parent, wx.ID_ANY, messages.problemMessage, (320, 330), style = wx.ALIGN_CENTRE)
        self.problemMessage.SetFont(wx.Font(config.fontSize[1], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.problemMessage.SetBackgroundColour(config.backgroundColour)

        answerImg = wx.Bitmap(join(config.coreImagesPath, 'ansBlank.png'), wx.BITMAP_TYPE_PNG)
        self.answerImage = wx.StaticBitmap(parent, -1, answerImg, (100,330), (180,140))
        self.answerImage.SetBackgroundColour(config.backgroundColour)

    def nextQuestion(self, answer, questionImgList):
        if len(self.eventQueue) != 0:
            self.eventQueue[0].SetBackgroundColour(config.backgroundColour)
            self.eventQueue[0].SetBitmap(self.eventQueue[0].GetBitmap())
        self.eventQueue = []
        self.answer = answer
        self.answerImage.SetBitmap(wx.Bitmap(join(config.coreImagesPath, 'ansBlank.png'), wx.BITMAP_TYPE_PNG))
        self.questionImage0.SetBitmap(wx.BitmapFromImage(questionImgList[0]))
        self.questionImage1.SetBitmap(wx.BitmapFromImage(questionImgList[1]))
        self.questionImage2.SetBitmap(wx.BitmapFromImage(questionImgList[2]))
        self.questionImage3.SetBitmap(wx.BitmapFromImage(questionImgList[3]))
        self.questionImage4.SetBitmap(wx.BitmapFromImage(questionImgList[4]))

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
            self.eventQueue[0].SetBitmap(self.eventQueue[0].GetBitmap())
        elif len(self.eventQueue) == 2:
            self.eventQueue[0].SetBackgroundColour(config.backgroundColour)
            self.eventQueue[0].SetBitmap(self.eventQueue[0].GetBitmap())
            self.eventQueue.pop(0)
            self.eventQueue[0].SetBackgroundColour(config.fillColour)
            self.eventQueue[0].SetBitmap(self.eventQueue[0].GetBitmap())

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
