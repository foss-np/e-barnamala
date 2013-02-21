import wx
import wx.lib.stattext as statTex
import random
import conf.config as config
import conf.messages as messages
from os.path import join

class numberAnswerList():
    def __init__(self, parent, question, numberList):
        if wx.Platform != "__WXGTK__":
            statText = wx.StaticText
        else:
            statText = statTex.GenStaticText
        self.buttonPressed = -1
        self.question = question
        self.fontSize = config.fontSize[2]
        self.eventQueue = []
        self.numberList = numberList

        self.displayText0 = statText(parent, wx.ID_ANY, messages.searchAnswer, (610, 240), style = wx.ALIGN_CENTRE)
        self.displayText0.SetFont(wx.Font(config.fontSize[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText0.SetBackgroundColour(config.backgroundColour)
        
        self.displayText1 = statText(parent, wx.ID_ANY, self.checkNumber(self.numberList[0]), (90, 230), style = wx.ALIGN_CENTRE)
        self.displayText1.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText1.SetBackgroundColour(config.backgroundColour)
        self.displayText1.Bind(wx.EVT_LEFT_DOWN, self.OnAns1, id=self.displayText1.GetId())

        self.displayText2 = statText(parent, wx.ID_ANY, self.checkNumber(self.numberList[1]), (140, 230), style = wx.ALIGN_CENTRE)
        self.displayText2.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText2.SetBackgroundColour(config.backgroundColour)
        self.displayText2.Bind(wx.EVT_LEFT_DOWN, self.OnAns2, id=self.displayText2.GetId())

        self.displayText3 = statText(parent, wx.ID_ANY, self.checkNumber(self.numberList[2]), (190, 230), style = wx.ALIGN_CENTRE)
        self.displayText3.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText3.SetBackgroundColour(config.backgroundColour)
        self.displayText3.Bind(wx.EVT_LEFT_DOWN, self.OnAns3, id=self.displayText3.GetId())

        self.displayText4 = statText(parent, wx.ID_ANY, self.checkNumber(self.numberList[3]), (240, 230), style = wx.ALIGN_CENTRE)
        self.displayText4.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText4.SetBackgroundColour(config.backgroundColour)
        self.displayText4.Bind(wx.EVT_LEFT_DOWN, self.OnAns4, id=self.displayText4.GetId())

        self.displayText5 = statText(parent, wx.ID_ANY, self.checkNumber(self.numberList[4]), (290, 230), style = wx.ALIGN_CENTRE)
        self.displayText5.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText5.SetBackgroundColour(config.backgroundColour)
        self.displayText5.Bind(wx.EVT_LEFT_DOWN, self.OnAns5, id=self.displayText5.GetId())

        self.displayText6 = statText(parent, wx.ID_ANY, self.checkNumber(self.numberList[5]), (340, 230), style = wx.ALIGN_CENTRE)
        self.displayText6.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText6.SetBackgroundColour(config.backgroundColour)
        self.displayText6.Bind(wx.EVT_LEFT_DOWN, self.OnAns6, id=self.displayText6.GetId())

        self.displayText7 = statText(parent, wx.ID_ANY, self.checkNumber(self.numberList[6]), (390, 230), style = wx.ALIGN_CENTRE)
        self.displayText7.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText7.SetBackgroundColour(config.backgroundColour)
        self.displayText7.Bind(wx.EVT_LEFT_DOWN, self.OnAns7, id=self.displayText7.GetId())

        self.displayText8 = statText(parent, wx.ID_ANY, self.checkNumber(self.numberList[7]), (440, 230), style = wx.ALIGN_CENTRE)
        self.displayText8.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText8.SetBackgroundColour(config.backgroundColour)
        self.displayText8.Bind(wx.EVT_LEFT_DOWN, self.OnAns8, id=self.displayText8.GetId())

        self.displayText9 = statText(parent, wx.ID_ANY, self.checkNumber(self.numberList[8]), (490, 230), style = wx.ALIGN_CENTRE)
        self.displayText9.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText9.SetBackgroundColour(config.backgroundColour)
        self.displayText9.Bind(wx.EVT_LEFT_DOWN, self.OnAns9, id=self.displayText9.GetId())

        self.displayText10 = statText(parent, wx.ID_ANY, self.checkNumber(self.numberList[9]), (540, 230), style = wx.ALIGN_CENTRE)
        self.displayText10.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText10.SetBackgroundColour(config.backgroundColour)
        self.displayText10.Bind(wx.EVT_LEFT_DOWN, self.OnAns10, id=self.displayText10.GetId())

        answerImg = wx.Bitmap(join(config.coreImagesPath, 'ansBlank.png'), wx.BITMAP_TYPE_PNG)
        self.answerImage = wx.StaticBitmap(parent, -1, answerImg, (100,325), (180,140))
        self.answerImage.SetBackgroundColour(config.backgroundColour)

    def nextQuestion(self, question, numberList):
        self.question = question
        self.numberList = numberList
        if len(self.eventQueue) != 0:
            self.eventQueue[0].SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.eventQueue = []
        self.answerImage.SetBitmap(wx.Bitmap(join(config.coreImagesPath, 'ansBlank.png'), wx.BITMAP_TYPE_PNG))
        ###below done on the hope that one day the display of list will be set to random
        self.displayText1.SetLabel(self.checkNumber(self.numberList[0]))
        self.displayText2.SetLabel(self.checkNumber(self.numberList[1]))
        self.displayText3.SetLabel(self.checkNumber(self.numberList[2]))
        self.displayText4.SetLabel(self.checkNumber(self.numberList[3]))
        self.displayText5.SetLabel(self.checkNumber(self.numberList[4]))
        self.displayText6.SetLabel(self.checkNumber(self.numberList[5]))
        self.displayText7.SetLabel(self.checkNumber(self.numberList[6]))
        self.displayText8.SetLabel(self.checkNumber(self.numberList[7]))
        self.displayText9.SetLabel(self.checkNumber(self.numberList[8]))
        self.displayText10.SetLabel(self.checkNumber(self.numberList[9]))

    def OnAns1(self, event):
        self.eventQueue.append(event.GetEventObject())
        self.buttonPressed = 0
        self.changeFontSize()
        answer = self.checkAnswer()
        self.displayResult(answer)

    def OnAns2(self, event):
        self.eventQueue.append(event.GetEventObject())
        self.buttonPressed = 1
        self.changeFontSize()
        answer = self.checkAnswer()
        self.displayResult(answer)

    def OnAns3(self, event):
        self.eventQueue.append(event.GetEventObject())
        self.buttonPressed = 2
        self.changeFontSize()
        answer = self.checkAnswer()
        self.displayResult(answer)

    def OnAns4(self, event):
        self.eventQueue.append(event.GetEventObject())
        self.buttonPressed = 3
        self.changeFontSize()
        answer = self.checkAnswer()
        self.displayResult(answer)

    def OnAns5(self, event):
        self.eventQueue.append(event.GetEventObject())
        self.buttonPressed = 4
        self.changeFontSize()
        answer = self.checkAnswer()
        self.displayResult(answer)

    def OnAns6(self, event):
        self.eventQueue.append(event.GetEventObject())
        self.buttonPressed = 5
        self.changeFontSize()
        answer = self.checkAnswer()
        self.displayResult(answer)

    def OnAns7(self, event):
        self.eventQueue.append(event.GetEventObject())
        self.buttonPressed = 6
        self.changeFontSize()
        answer = self.checkAnswer()
        self.displayResult(answer)

    def OnAns8(self, event):
        self.eventQueue.append(event.GetEventObject())
        self.buttonPressed = 7
        self.changeFontSize()
        answer = self.checkAnswer()
        self.displayResult(answer)

    def OnAns9(self, event):
        self.eventQueue.append(event.GetEventObject())
        self.buttonPressed = 8
        self.changeFontSize()
        answer = self.checkAnswer()
        self.displayResult(answer)

    def OnAns10(self, event):
        self.eventQueue.append(event.GetEventObject())
        self.buttonPressed = 9
        self.changeFontSize()
        answer = self.checkAnswer()
        self.displayResult(answer)

    def changeFontSize(self):
        if len(self.eventQueue) == 1:
            self.eventQueue[0].SetFont(wx.Font(65, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        elif len(self.eventQueue) == 2:
            self.eventQueue[0].SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
            self.eventQueue.pop(0)
            self.eventQueue[0].SetFont(wx.Font(65, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))

    def checkAnswer(self):
        answer = ''
        if self.question == self.numberList[self.buttonPressed] :
            answer = "Right"
        else:
            answer = "Wrong"
        return answer

    def displayResult(self, answer):
        if answer == "Right":
            self.answerImage.SetBitmap(wx.Bitmap(join(config.coreImagesPath, 'right.png'), wx.BITMAP_TYPE_PNG))
        else:
            self.answerImage.SetBitmap(wx.Bitmap(join(config.coreImagesPath, 'wrong.png'), wx.BITMAP_TYPE_PNG))

##  this function is different from other similar function because when using the original numberList, it was getting changed. This
##  same instance was used in other places thereby loosing 1 & from && for the number 7. This was a problem in Linux only.
    def checkNumber(self, number):
        if wx.Platform == "__WXGTK__":
            if len(number) > 1:
                number = number[0]
        else:
            pass
        return number
