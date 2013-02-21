import wx
import wx.lib.statbmp as statbp
import conf.config as config
import utils.charActivitiesUtils as nGUtils
import utils.bottomMenu as bottomMenu
from os.path import join

class charImageMatch(wx.Panel):
    def __init__(self, parent, id, mainWin, mainPanel, currentLesson):
        if wx.Platform != "__WXGTK__":
            statbmp = wx.StaticBitmap
        else:
            statbmp = statbp.GenStaticBitmap
        self.mainWin = mainWin
        self.mainPanel = mainPanel
        self.currentLesson = currentLesson
        self.buttonPressed = 20
        self.question = ''
        self.eventQueue = []

        self.question, self.answerList, self.answerImageList = nGUtils.nextImageMatchQuestion(self.currentLesson)

        self.fontSize = config.fontSize[4]
        if currentLesson == 'aaa': self.fontSize = config.fontSize[4]
        if currentLesson == 'kaKha': self.fontSize = config.fontSize[4]
        if currentLesson == 'oneTwo': self.fontSize = config.fontSize[5]
        if currentLesson == 'time': self.fontSize = config.fontSize[4]
        
        self.displayPanel = wx.Panel(parent, -1, (0, 0), (800, 600))
        self.displayPanel.SetBackgroundColour(config.backgroundColour)

        self.displayText = wx.StaticText(self.displayPanel, -1, self.question, (20, 70), style = wx.ALIGN_CENTRE)
        self.displayText.SetFont(wx.Font(self.fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayText.SetBackgroundColour(config.backgroundColour)

        displayImg = wx.Bitmap(join(config.coreImagesPath, 'divider.png'), wx.BITMAP_TYPE_PNG)
        self.displayImage = wx.StaticBitmap(self.displayPanel, -1, displayImg, (200,80), (displayImg.GetWidth(), displayImg.GetHeight()))
        self.displayImage.SetBackgroundColour(config.backgroundColour)

        ansImg1 = wx.Bitmap(self.answerImageList[0], wx.BITMAP_TYPE_PNG)
        self.answerImage1 = statbmp(self.displayPanel, 1, ansImg1, (260,90), (ansImg1.GetWidth(), ansImg1.GetHeight()))
        self.answerImage1.SetBackgroundColour(config.backgroundColour)
        self.answerImage1.Bind(wx.EVT_LEFT_DOWN, self.OnAns1, id=1)

        ansImg2 = wx.Bitmap(self.answerImageList[1], wx.BITMAP_TYPE_PNG)
        self.answerImage2 = statbmp(self.displayPanel, 2, ansImg2, (440,90), (ansImg2.GetWidth(), ansImg2.GetHeight()))
        self.answerImage2.SetBackgroundColour(config.backgroundColour)
        self.answerImage2.Bind(wx.EVT_LEFT_DOWN, self.OnAns2, id=2)

        ansImg3 = wx.Bitmap(self.answerImageList[2], wx.BITMAP_TYPE_PNG)
        self.answerImage3 = statbmp(self.displayPanel, 3, ansImg3, (620,90), (ansImg3.GetWidth(), ansImg3.GetHeight()))
        self.answerImage3.SetBackgroundColour(config.backgroundColour)
        self.answerImage3.Bind(wx.EVT_LEFT_DOWN, self.OnAns3, id=3)

        answerImg = wx.Bitmap(join(config.coreImagesPath, 'ansBlank.png'), wx.BITMAP_TYPE_PNG)
        self.answerImage = wx.StaticBitmap(self.displayPanel, -1, answerImg, (150,300), (180,140))
        self.answerImage.SetBackgroundColour(config.backgroundColour)

        nextQuestionImg = wx.Bitmap(join(config.buttonsPath,'nextQuestion.png'), wx.BITMAP_TYPE_PNG)
        self.nextQuestionButton = wx.BitmapButton(self.displayPanel, 4, nextQuestionImg, (460,320), style = wx.NO_BORDER)
        self.nextQuestionButton.SetBackgroundColour(config.backgroundColour)
        self.nextQuestionButton.Bind(wx.EVT_BUTTON, self.OnNextQuestion, id=4)

        bottomMenu.bottomMenu([self.displayPanel], parent, self.mainWin, 'threeButton', self.mainPanel)
        
    def OnNextQuestion(self, event=None):
        if len(self.eventQueue) != 0:
            self.eventQueue[0].SetBackgroundColour(config.backgroundColour)
            self.eventQueue[0].SetBitmap(self.eventQueue[0].GetBitmap())
        self.eventQueue = []
        self.answerImage.SetBitmap(wx.Bitmap(join(config.coreImagesPath, 'ansBlank.png'), wx.BITMAP_TYPE_PNG))
        self.question, self.answerList, self.answerImageList = nGUtils.nextImageMatchQuestion(self.currentLesson)
        self.displayText.SetLabel(self.question)
        self.answerImage1.SetBitmap(wx.Bitmap(self.answerImageList[0], wx.BITMAP_TYPE_PNG))
        self.answerImage2.SetBitmap(wx.Bitmap(self.answerImageList[1], wx.BITMAP_TYPE_PNG))
        self.answerImage3.SetBitmap(wx.Bitmap(self.answerImageList[2], wx.BITMAP_TYPE_PNG))

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
            self.eventQueue[0].SetBitmap(self.eventQueue[0].GetBitmap())
        elif len(self.eventQueue) == 2:
            self.eventQueue[0].SetBackgroundColour(config.backgroundColour)
            self.eventQueue[0].SetBitmap(self.eventQueue[0].GetBitmap())
            self.eventQueue.pop(0)
            self.eventQueue[0].SetBackgroundColour(config.fillColour)
            self.eventQueue[0].SetBitmap(self.eventQueue[0].GetBitmap())

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
    
                              
