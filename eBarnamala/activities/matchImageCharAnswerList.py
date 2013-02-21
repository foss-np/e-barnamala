import wx
import wx.lib.statbmp as statbp
import wx.lib.stattext as statTex
import random
import conf.config as config
import conf.messages as messages
from os.path import join
import Image

class matchImageCharAnswerList():
    def __init__(self, parent, questionList, questionImgList, answerList, answerNepaliList, currentLesson):
        if wx.Platform != "__WXGTK__":
            statbmp = wx.StaticBitmap
            statText = wx.StaticText
        else:
            statbmp = statbp.GenStaticBitmap
            statText = statTex.GenStaticText
        self.firstButtonPressed = -1
        self.secondButtonPressed = -1
        self.dataType = []
        self.questionList = questionList
        self.questionImgList = questionImgList
        self.answerList = answerList
        self.answerNepaliList = answerNepaliList
        self.currentLesson = currentLesson
        if self.currentLesson in ['oneTwo', 'time']:
            self.checkNumberSet()
        self. eventObjectList = []
        if currentLesson in ['aaa','kaKha','oneTwo']:
            self.fontSize = config.fontSize[3]
        elif currentLesson in ['time']:
            self.fontSize = config.fontSize[2]
        else:
            self.fontSize = config.fontSize[0]

        questionImg0 = wx.BitmapFromImage(self.questionImgList[0])
        self.questionImage0 = statbmp(parent, wx.ID_ANY, questionImg0, (40,70), (questionImg0.GetWidth(), questionImg0.GetHeight()))
        self.questionImage0.SetBackgroundColour(config.backgroundColour)
        self.questionImage0.Bind(wx.EVT_LEFT_DOWN, self.OnAns1, id=self.questionImage0.GetId())

        questionImg1 = wx.BitmapFromImage(self.questionImgList[1])
        self.questionImage1 = statbmp(parent, wx.ID_ANY, questionImg1, (180,70), (questionImg1.GetWidth(), questionImg1.GetHeight()))
        self.questionImage1.SetBackgroundColour(config.backgroundColour)
        self.questionImage1.Bind(wx.EVT_LEFT_DOWN, self.OnAns2, id=self.questionImage1.GetId())

        questionImg2 = wx.BitmapFromImage(self.questionImgList[2])
        self.questionImage2 = statbmp(parent, wx.ID_ANY, questionImg2, (330,70), (questionImg2.GetWidth(), questionImg2.GetHeight()))
        self.questionImage2.SetBackgroundColour(config.backgroundColour)
        self.questionImage2.Bind(wx.EVT_LEFT_DOWN, self.OnAns3, id=self.questionImage2.GetId())

        questionImg3 = wx.BitmapFromImage(self.questionImgList[3])
        self.questionImage3 = statbmp(parent, wx.ID_ANY, questionImg3, (470,70), (questionImg3.GetWidth(), questionImg3.GetHeight()))
        self.questionImage3.SetBackgroundColour(config.backgroundColour)
        self.questionImage3.Bind(wx.EVT_LEFT_DOWN, self.OnAns4, id=self.questionImage3.GetId())

        questionImg4 = wx.BitmapFromImage(self.questionImgList[4])
        self.questionImage4 = statbmp(parent, wx.ID_ANY, questionImg4, (620,70), (questionImg4.GetWidth(), questionImg4.GetHeight()))
        self.questionImage4.SetBackgroundColour(config.backgroundColour)
        self.questionImage4.Bind(wx.EVT_LEFT_DOWN, self.OnAns5, id=self.questionImage4.GetId())

        self.displayText0 = statText(parent, wx.ID_ANY, self.answerNepaliList[0], (40,250), style = wx.ALIGN_CENTRE)
        self.displayText0.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText0.SetBackgroundColour(config.backgroundColour)
        self.displayText0.Bind(wx.EVT_LEFT_DOWN, self.OnAns6, id=self.displayText0.GetId())

        self.displayText1 = statText(parent, wx.ID_ANY, self.answerNepaliList[1], (180,250), style = wx.ALIGN_CENTRE)
        self.displayText1.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText1.SetBackgroundColour(config.backgroundColour)
        self.displayText1.Bind(wx.EVT_LEFT_DOWN, self.OnAns7, id=self.displayText1.GetId())

        self.displayText2 = statText(parent, wx.ID_ANY, self.answerNepaliList[2], (330,250), style = wx.ALIGN_CENTRE)
        self.displayText2.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText2.SetBackgroundColour(config.backgroundColour)
        self.displayText2.Bind(wx.EVT_LEFT_DOWN, self.OnAns8, id=self.displayText2.GetId())

        self.displayText3 = statText(parent, wx.ID_ANY, self.answerNepaliList[3], (470,250), style = wx.ALIGN_CENTRE)
        self.displayText3.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText3.SetBackgroundColour(config.backgroundColour)
        self.displayText3.Bind(wx.EVT_LEFT_DOWN, self.OnAns9, id=self.displayText3.GetId())

        self.displayText4 = statText(parent, wx.ID_ANY, self.answerNepaliList[4], (620,250), style = wx.ALIGN_CENTRE)
        self.displayText4.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText4.SetBackgroundColour(config.backgroundColour)
        self.displayText4.Bind(wx.EVT_LEFT_DOWN, self.OnAns10, id=self.displayText4.GetId())

    def nextQuestion(self, questionList, questionImgList, answerList, answerNepaliList):
        self.questionList = questionList
        self.answerList = answerList
        self.answerNepaliList = answerNepaliList
        self.dataType = []
        self.eventObjectList = []
        if self.currentLesson in ['oneTwo', 'time']:
            self.checkNumberSet()
        
        self.questionImage0.Show(True)
        self.questionImage0.SetBackgroundColour(config.backgroundColour)
        self.questionImage0.SetBitmap(wx.BitmapFromImage(questionImgList[0]))

        self.questionImage1.Show(True)
        self.questionImage1.SetBackgroundColour(config.backgroundColour)
        self.questionImage1.SetBitmap(wx.BitmapFromImage(questionImgList[1]))

        self.questionImage2.Show(True)
        self.questionImage2.SetBackgroundColour(config.backgroundColour)
        self.questionImage2.SetBitmap(wx.BitmapFromImage(questionImgList[2]))

        self.questionImage3.Show(True)
        self.questionImage3.SetBackgroundColour(config.backgroundColour)
        self.questionImage3.SetBitmap(wx.BitmapFromImage(questionImgList[3]))

        self.questionImage4.Show(True)
        self.questionImage4.SetBackgroundColour(config.backgroundColour)
        self.questionImage4.SetBitmap(wx.BitmapFromImage(questionImgList[4]))

        self.displayText0.Show(True)
        self.displayText1.Show(True)
        self.displayText2.Show(True)
        self.displayText3.Show(True)
        self.displayText4.Show(True)
        self.displayText0.SetBackgroundColour(config.backgroundColour)
        self.displayText1.SetBackgroundColour(config.backgroundColour)
        self.displayText2.SetBackgroundColour(config.backgroundColour)
        self.displayText3.SetBackgroundColour(config.backgroundColour)
        self.displayText4.SetBackgroundColour(config.backgroundColour)
        self.displayText0.SetLabel(self.answerNepaliList[0])
        self.displayText1.SetLabel(self.answerNepaliList[1])
        self.displayText2.SetLabel(self.answerNepaliList[2])
        self.displayText3.SetLabel(self.answerNepaliList[3])
        self.displayText4.SetLabel(self.answerNepaliList[4])
        
    def OnAns1(self, event):
        self.firstButtonPressed = 0
        self.dataType.append("img")
        self.eventObjectList.append(event.GetEventObject())
        self.changeBackground()
        self.checkAnswer()
        
    def OnAns2(self, event):
        self.firstButtonPressed = 1
        self.dataType.append("img")
        self.eventObjectList.append(event.GetEventObject())
        self.changeBackground()
        self.checkAnswer()
        
    def OnAns3(self, event):
        self.firstButtonPressed = 2
        self.dataType.append("img")
        self.eventObjectList.append(event.GetEventObject())
        self.changeBackground()
        self.checkAnswer()
        
    def OnAns4(self, event):
        self.firstButtonPressed = 3
        self.dataType.append("img")
        self.eventObjectList.append(event.GetEventObject())
        self.changeBackground()
        self.checkAnswer()
        
    def OnAns5(self, event):
        self.firstButtonPressed = 4
        self.dataType.append("img")
        self.eventObjectList.append(event.GetEventObject())
        self.changeBackground()
        self.checkAnswer()

    def OnAns6(self, event):
        self.secondButtonPressed = 0
        self.dataType.append("char")
        self.eventObjectList.append(event.GetEventObject())
        self.changeBackground()
        self.checkAnswer()

    def OnAns7(self, event):
        self.secondButtonPressed = 1
        self.dataType.append("char")
        self.eventObjectList.append(event.GetEventObject())
        self.changeBackground()
        self.checkAnswer()

    def OnAns8(self, event):
        self.secondButtonPressed = 2
        self.dataType.append("char")
        self.eventObjectList.append(event.GetEventObject())
        self.changeBackground()
        self.checkAnswer()

    def OnAns9(self, event):
        self.secondButtonPressed = 3
        self.dataType.append("char")
        self.eventObjectList.append(event.GetEventObject())
        self.changeBackground()
        self.checkAnswer()

    def OnAns10(self, event):
        self.secondButtonPressed = 4
        self.dataType.append("char")
        self.eventObjectList.append(event.GetEventObject())
        self.changeBackground()
        self.checkAnswer()

    def changeBackground(self):
        if len(self.dataType) == 1 and len(self.eventObjectList) == 1:
            if self.dataType[0] == "img":
                self.eventObjectList[0].SetBackgroundColour(config.fillColour)
                self.eventObjectList[0].SetBitmap(self.eventObjectList[0].GetBitmap())
            if self.dataType[0] == "char":
                self.eventObjectList[0].SetBackgroundColour(config.fillColour)
                self.eventObjectList[0].SetLabel(self.eventObjectList[0].GetLabel())    
                
        elif len(self.dataType) == 2 and len(self.eventObjectList) == 2:
            if (self.dataType[0] == "img" and self.dataType[1] == "img") or (self.dataType[0] == "char" and self.dataType[1] == "char"):
                self.eventObjectList[0].SetBackgroundColour(config.backgroundColour)
                self.eventObjectList[1].SetBackgroundColour(config.backgroundColour)
                try:
                    self.eventObjectList[0].SetBitmap(self.eventObjectList[0].GetBitmap())
                    self.eventObjectList[1].SetBitmap(self.eventObjectList[1].GetBitmap())
                except:
                    self.eventObjectList[0].SetLabel(self.eventObjectList[0].GetLabel())
                    self.eventObjectList[1].SetLabel(self.eventObjectList[1].GetLabel())
                self.dataType = []
                self.firstButtonPressed = -1
                self.secondButtonPressed = -1
                self.eventObjectList = []
            elif (self.dataType[0] == "img" and self.dataType[1] == "char") or (self.dataType[0] == "char" and self.dataType[1] == "img"):
                self.eventObjectList[0].SetBackgroundColour(config.backgroundColour)
                self.eventObjectList[1].SetBackgroundColour(config.backgroundColour)
                try:
                    self.eventObjectList[0].SetBitmap(self.eventObjectList[0].GetBitmap())
                    self.eventObjectList[1].SetBitmap(self.eventObjectList[1].GetBitmap())
                except:
                    self.eventObjectList[0].SetLabel(self.eventObjectList[0].GetLabel())
                    self.eventObjectList[1].SetLabel(self.eventObjectList[1].GetLabel())
                self.dataType = []
    
    def checkAnswer(self):
        if (self.firstButtonPressed != -1) and (self.secondButtonPressed != -1):
            if (self.answerList[self.secondButtonPressed] == self.questionList[self.firstButtonPressed]) :
                self.eventObjectList[0].Show(False)
                self.eventObjectList[1].Show(False)
                self.answerList[self.secondButtonPressed] = ''
                self.answerNepaliList[self.secondButtonPressed] = ''
                self.questionList[self.firstButtonPressed] = ''
                self.questionImgList[self.firstButtonPressed] = None
                self.firstButtonPressed = -1
                self.secondButtonPressed = -1
                self.eventObjectList = []
            elif (self.answerList[self.secondButtonPressed] != self.questionList[self.firstButtonPressed]) :
                self.firstButtonPressed = -1
                self.secondButtonPressed = -1
                self.eventObjectList = []
        else:
            pass

##  This function is to check for double printing of chars like && in Linux.
##  The function is kept here to solve problems occuring only in specific modules like this one.
    def checkNumberSet(self):
        if wx.Platform == "__WXGTK__":
            for i in range(len(self.answerNepaliList)):
                if self.answerNepaliList[i] == '&&':
                    self.answerNepaliList[i] = self.answerNepaliList[i][0]
        else:
            pass
                    
