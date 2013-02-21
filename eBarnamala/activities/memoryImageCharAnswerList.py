import wx
import wx.lib.statbmp as statbp
import wx.lib.stattext as statTex
import random
import conf.config as config
import conf.messages as messages
from os.path import join
import Image

class memoryImageCharAnswerList():
    def __init__(self, parent, questionList, questionImgList, answerList, answerNepaliList, currentLesson):
        if wx.Platform != "__WXGTK__":
            statbmp = wx.StaticBitmap
            statText = wx.StaticText
        else:
            statbmp = statbp.GenStaticBitmap
            statText = statTex.GenStaticText
        self.currentLesson = currentLesson
        self.buttonPressed = []
        self.questionList = questionList
        self.answerList = answerList
        self.answerNepaliList = answerNepaliList
        self.eventObjectList = []
        if self.currentLesson in ['oneTwo','time']:
            self.checkNumberSet()
        else:
            pass
        tempImageList = self.generateCardList(questionImgList, "img")
        tempCharList = self.generateCardList(answerNepaliList, "char")
        tempImageList, tempCharList = self.randomizeLists(tempImageList, tempCharList)
        self.imgList = tempImageList + tempCharList

        questionImg0 = wx.BitmapFromImage(self.makeCard("img", "back"))
        self.questionImage0 = statbmp(parent, wx.ID_ANY, questionImg0, (40,30), (questionImg0.GetWidth(), questionImg0.GetHeight()))
        self.questionImage0.SetBackgroundColour(config.backgroundColour)
        self.questionImage0.Bind(wx.EVT_LEFT_DOWN, self.OnAns1, id=self.questionImage0.GetId())

        self.questionImage1 = statbmp(parent, wx.ID_ANY, questionImg0, (180,30), (questionImg0.GetWidth(), questionImg0.GetHeight()))
        self.questionImage1.SetBackgroundColour(config.backgroundColour)
        self.questionImage1.Bind(wx.EVT_LEFT_DOWN, self.OnAns2, id=self.questionImage1.GetId())

        self.questionImage2 = statbmp(parent, wx.ID_ANY, questionImg0, (330,30), (questionImg0.GetWidth(), questionImg0.GetHeight()))
        self.questionImage2.SetBackgroundColour(config.backgroundColour)
        self.questionImage2.Bind(wx.EVT_LEFT_DOWN, self.OnAns3, id=self.questionImage2.GetId())

        self.questionImage3 = statbmp(parent, wx.ID_ANY, questionImg0, (470,30), (questionImg0.GetWidth(), questionImg0.GetHeight()))
        self.questionImage3.SetBackgroundColour(config.backgroundColour)
        self.questionImage3.Bind(wx.EVT_LEFT_DOWN, self.OnAns4, id=self.questionImage3.GetId())

        self.questionImage4 = statbmp(parent, wx.ID_ANY, questionImg0, (620,30), (questionImg0.GetWidth(), questionImg0.GetHeight()))
        self.questionImage4.SetBackgroundColour(config.backgroundColour)
        self.questionImage4.Bind(wx.EVT_LEFT_DOWN, self.OnAns5, id=self.questionImage4.GetId())

        self.questionImage5 = statbmp(parent, wx.ID_ANY, questionImg0, (40,220), (questionImg0.GetWidth(), questionImg0.GetHeight()))
        self.questionImage5.SetBackgroundColour(config.backgroundColour)
        self.questionImage5.Bind(wx.EVT_LEFT_DOWN, self.OnAns6, id=self.questionImage5.GetId())

        self.questionImage6 = statbmp(parent, wx.ID_ANY, questionImg0, (180,220), (questionImg0.GetWidth(), questionImg0.GetHeight()))
        self.questionImage6.SetBackgroundColour(config.backgroundColour)
        self.questionImage6.Bind(wx.EVT_LEFT_DOWN, self.OnAns7, id=self.questionImage6.GetId())

        self.questionImage7 = statbmp(parent, wx.ID_ANY, questionImg0, (330,220), (questionImg0.GetWidth(), questionImg0.GetHeight()))
        self.questionImage7.SetBackgroundColour(config.backgroundColour)
        self.questionImage7.Bind(wx.EVT_LEFT_DOWN, self.OnAns8, id=self.questionImage7.GetId())

        self.questionImage8 = statbmp(parent, wx.ID_ANY, questionImg0, (470,220), (questionImg0.GetWidth(), questionImg0.GetHeight()))
        self.questionImage8.SetBackgroundColour(config.backgroundColour)
        self.questionImage8.Bind(wx.EVT_LEFT_DOWN, self.OnAns9, id=self.questionImage8.GetId())

        self.questionImage9 = statbmp(parent, wx.ID_ANY, questionImg0, (620,220), (questionImg0.GetWidth(), questionImg0.GetHeight()))
        self.questionImage9.SetBackgroundColour(config.backgroundColour)
        self.questionImage9.Bind(wx.EVT_LEFT_DOWN, self.OnAns10, id=self.questionImage9.GetId())

    def nextQuestion(self, questionList, questionImgList, answerList, answerNepaliList):
        self.questionList = questionList
        self.answerList = answerList
        self.answerNepaliList = answerNepaliList
        self.dataType = []
        self.eventObjectList = []

        self.eventObjectList = []
        self.buttonPressed = []
        if self.currentLesson in ['oneTwo','time']:
            self.checkNumberSet()
        else:
            pass

        tempImageList = self.generateCardList(questionImgList, "img")
        tempCharList = self.generateCardList(answerNepaliList, "char")
        questionImg0 = self.makeCard("img", "back")
        tempImageList, tempCharList = self.randomizeLists(tempImageList, tempCharList)
        self.imgList = tempImageList + tempCharList
        
        self.questionImage0.Show(True)
        self.questionImage0.SetBackgroundColour(config.backgroundColour)
        self.questionImage0.SetBitmap(wx.BitmapFromImage(questionImg0))
        
        self.questionImage1.Show(True)
        self.questionImage1.SetBackgroundColour(config.backgroundColour)
        self.questionImage1.SetBitmap(wx.BitmapFromImage(questionImg0))

        self.questionImage2.Show(True)
        self.questionImage2.SetBackgroundColour(config.backgroundColour)
        self.questionImage2.SetBitmap(wx.BitmapFromImage(questionImg0))

        self.questionImage3.Show(True)
        self.questionImage3.SetBackgroundColour(config.backgroundColour)
        self.questionImage3.SetBitmap(wx.BitmapFromImage(questionImg0))

        self.questionImage4.Show(True)
        self.questionImage4.SetBackgroundColour(config.backgroundColour)
        self.questionImage4.SetBitmap(wx.BitmapFromImage(questionImg0))

        self.questionImage5.Show(True)
        self.questionImage5.SetBackgroundColour(config.backgroundColour)
        self.questionImage5.SetBitmap(wx.BitmapFromImage(questionImg0))

        self.questionImage6.Show(True)
        self.questionImage6.SetBackgroundColour(config.backgroundColour)
        self.questionImage6.SetBitmap(wx.BitmapFromImage(questionImg0))

        self.questionImage7.Show(True)
        self.questionImage7.SetBackgroundColour(config.backgroundColour)
        self.questionImage7.SetBitmap(wx.BitmapFromImage(questionImg0))

        self.questionImage8.Show(True)
        self.questionImage8.SetBackgroundColour(config.backgroundColour)
        self.questionImage8.SetBitmap(wx.BitmapFromImage(questionImg0))

        self.questionImage9.Show(True)
        self.questionImage9.SetBackgroundColour(config.backgroundColour)
        self.questionImage9.SetBitmap(wx.BitmapFromImage(questionImg0))

        
        
    def OnAns1(self, event):
        self.buttonPressed.append(0)
        self.eventObjectList.append(event.GetEventObject())
        self.changeBackground()
        
    def OnAns2(self, event):
        self.buttonPressed.append(1)
        self.eventObjectList.append(event.GetEventObject())
        self.changeBackground()
        
    def OnAns3(self, event):
        self.buttonPressed.append(2)
        self.eventObjectList.append(event.GetEventObject())
        self.changeBackground()
        
    def OnAns4(self, event):
        self.buttonPressed.append(3)
        self.eventObjectList.append(event.GetEventObject())
        self.changeBackground()
        
    def OnAns5(self, event):
        self.buttonPressed.append(4)
        self.eventObjectList.append(event.GetEventObject())
        self.changeBackground()
        
    def OnAns6(self, event):
        self.buttonPressed.append(5)
        self.eventObjectList.append(event.GetEventObject())
        self.changeBackground()
        
    def OnAns7(self, event):
        self.buttonPressed.append(6)
        self.eventObjectList.append(event.GetEventObject())
        self.changeBackground()
        
    def OnAns8(self, event):
        self.buttonPressed.append(7)
        self.eventObjectList.append(event.GetEventObject())
        self.changeBackground()
        
    def OnAns9(self, event):
        self.buttonPressed.append(8)
        self.eventObjectList.append(event.GetEventObject())
        self.changeBackground()
        
    def OnAns10(self, event):
        self.buttonPressed.append(9)
        self.eventObjectList.append(event.GetEventObject())
        self.changeBackground()
        
    def changeBackground(self):
        if len(self.buttonPressed) == 1:
            self.eventObjectList[0].SetBitmap(wx.BitmapFromImage(self.imgList[int(self.buttonPressed[0])]))
        if len(self.buttonPressed) == 2:
            if self.buttonPressed[0] != self.buttonPressed[1]:
                self.eventObjectList[1].SetBitmap(wx.BitmapFromImage(self.imgList[int(self.buttonPressed[1])]))
                #wx.CallLater(1000,self.checkAnswer)
                self.checkAnswer()
            else:
                self.buttonPressed.pop(0)
                self.eventObjectList[0].SetBitmap(wx.BitmapFromImage(self.makeCard("img", "back")))
                self.buttonPressed.pop(0)
                self.eventObjectList = []
                
        if len(self.buttonPressed) > 2:
            self.eventObjectList = []
            self.buttonPressed = []
            
    def checkAnswer(self):
        if (len(self.buttonPressed) == 2) and (self.buttonPressed[0] != self.buttonPressed[1]):
            totalList = self.questionList + self.answerList
            if totalList[int(self.buttonPressed[0])] == totalList[int(self.buttonPressed[1])]:
                wx.CallLater(500, self.changeBitmap)
                self.buttonPressed = []                
            else:
                self.eventObjectList[0].SetBitmap(wx.BitmapFromImage(self.makeCard("img", "back")))
                self.eventObjectList.pop(0)
                self.buttonPressed.pop(0)
        else:
            self.eventObjectList = []
            self.buttonPressed = []
        if len(self.buttonPressed) > 2:
            self.eventObjectList = []
            self.buttonPressed = []

    def changeBitmap(self):
        self.eventObjectList[0].Show(False)
        self.eventObjectList[1].Show(False)
        self.eventObjectList = []
                
    def randomizeLists(self, tempImgList, tempCharList):
        randomCombo = [[1,3,4], [0,1,2,4], [1,3], [2,4], [0,2,3], [2,3], [2]]
        tempList = random.choice(randomCombo)
        for i in tempList:
            tempChar = self.questionList[i]
            tempImg = tempImgList[i]
            self.questionList[i] = self.answerList[i]
            tempImgList[i] = tempCharList[i]
            self.answerList[i] = tempChar
            tempCharList[i] = tempImg
        return tempImgList, tempCharList

##  This function is to check for double printing of chars like && in Linux.
##  The function is kept here to solve problems occuring only in specific modules like this one.
    def checkNumberSet(self):
        if wx.Platform == "__WXGTK__":
            for i in range(len(self.answerNepaliList)):
                if self.answerNepaliList[i] == '&&':
                    self.answerNepaliList[i] = self.answerNepaliList[i][0]
        else:
            pass

    def makeCard(self, toConvert, face): #personally dont know why I have done this
        baseImg = ''
        if (toConvert == "img") and (face == "back"):
            baseImg = Image.open(join(config.coreImagesPath, config.cardBackFace))
        returnImg = wx.EmptyImage(baseImg.size[0], baseImg.size[1])
        returnImg.SetData(baseImg.convert('RGB').tostring())
        returnImg.SetAlphaData(baseImg.convert("RGBA").tostring()[3::4])
        return returnImg

    def generateCardList(self, listToConvert, dataType):
        fontSize = 0
        if self.currentLesson in ['time', 'kaKha','aaa','oneTwo']:
            fontSize = config.fontSizeForCard + 25
        else:
            fontSize = config.fontSizeForCard
        imgReturnList = []
        if dataType == "img":
            for i in listToConvert:
                baseImg = Image.open(join(config.coreImagesPath, config.cardFrontFace))
                temp = Image.open(i)
                temp = temp.resize(((50*temp.size[0])/100,(50*temp.size[1])/100), Image.ANTIALIAS)
                background = Image.new('RGBA', temp.size, config.bckgndColour)
                background.paste(temp, temp)
                w, h = background.size[0], background.size[1]
                startx = (int(baseImg.size[0]) - int(w)) / 2
                starty = (int(baseImg.size[1]) - int(h)) / 2
                baseImg.paste(background.convert('RGBA'), (startx, starty))
                returnImg = wx.EmptyImage(baseImg.size[0], baseImg.size[1])
                returnImg.SetData(baseImg.convert('RGB').tostring())
                returnImg.SetAlphaData(baseImg.convert("RGBA").tostring()[3::4])
                imgReturnList.append(returnImg)
        if dataType == "char":
            for i in listToConvert:
                if i in ['&&']: ###temp fix for 77 trouble in winxp. Problem while writing to an image
                    i = i[0]
                else:
                    pass
                baseImg = wx.Bitmap(join(config.coreImagesPath, config.cardFrontFace), wx.BITMAP_TYPE_PNG)
                img = baseImg.ConvertToImage()
                img.ConvertAlphaToMask()
                baseImg = img.ConvertToBitmap()
                memory = wx.MemoryDC(baseImg)
                #memory.SelectObject(baseImg)
                memory.SetFont(wx.Font(fontSize, wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
                memory.SetTextForeground('red')#config.textColour)
                w, h = memory.GetTextExtent(i)
                startx = (int(baseImg.GetWidth()) - int(w)) / 2
                starty = (int(baseImg.GetHeight()) - int(h)) / 2
                memory.DrawText(i, startx, starty)
                imgReturnList.append(wx.ImageFromBitmap(baseImg))
        return imgReturnList
