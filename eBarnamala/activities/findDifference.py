import wx
import conf.config as config
import utils.findDifferenceUtils as findDifferenceUtils
import utils.bottomMenu as bottomMenu
import findDifferenceImageAnswerList
import findDifferenceAnswerList
from os.path import join
import Image

class findDifference():
    def __init__(self, parent, id, mainWin, mainPanel, currentLesson, gameType):
        self.mainWin = mainWin
        self.mainPanel = mainPanel
        self.currentLesson = currentLesson
        answer, answerList, answerImgList = 0, [], []
        self.answerImageList = ''
        self.gameType = gameType

        self.displayPanel = wx.Panel(parent, -1, (0, 0), (800, 600))
        self.displayPanel.SetBackgroundColour(config.backgroundColour)

        if (self.currentLesson == "animals" or self.currentLesson == "colour") and self.gameType == "Img":
            answer, answerImgList =findDifferenceUtils.nextFindDifferenceQuestion(self.currentLesson, self.gameType)
            answerImgList = resizeImage(answerImgList, 65)
            if self.currentLesson == "colour":
                answer, answerImgList = self.rotateImage(answer, answerImgList)
            else:
                pass
            self.answerImageList = findDifferenceImageAnswerList.imageAnswerList(self.displayPanel, answer, answerImgList)
        elif (self.currentLesson == "kaKha" or self.currentLesson == "aaa")  and self.gameType == "Char":
            answer, answerList = findDifferenceUtils.nextFindDifferenceQuestionWithoutImage(self.currentLesson, self.gameType)
            self.answerImageList = findDifferenceAnswerList.charAnswerList(self.displayPanel, answer, answerList)
        elif (self.currentLesson == "kaKha" or self.currentLesson == "aaa")  and self.gameType == "Img":
            answer, answerImgList =findDifferenceUtils.nextFindDifferenceQuestion(self.currentLesson, self.gameType)
            answerImgList = resizeImage(answerImgList, 65)
            self.answerImageList = findDifferenceImageAnswerList.imageAnswerList(self.displayPanel, answer, answerImgList)
        
        nextQuestionImg = wx.Bitmap(join(config.buttonsPath,'nextQuestion.png'), wx.BITMAP_TYPE_PNG)
        self.nextQuestionButton = wx.BitmapButton(self.displayPanel, 4, nextQuestionImg, (460,400), style = wx.NO_BORDER)
        self.nextQuestionButton.SetBackgroundColour(config.backgroundColour)
        self.nextQuestionButton.Bind(wx.EVT_BUTTON, self.OnNextQuestion, id=4)

        bottomMenu.bottomMenu([self.displayPanel], parent, self.mainWin, 'threeButton', self.mainPanel)
        
    def OnNextQuestion(self, event=None):
        answer, answerList, answerImgList = 0, [], []
        if (self.currentLesson == "animals" or self.currentLesson == "colour") and self.gameType == "Img":
            answer, answerImgList =findDifferenceUtils.nextFindDifferenceQuestion(self.currentLesson, self.gameType)
            answerImgList = resizeImage(answerImgList, 65)
            if self.currentLesson == "colour":
                answer, answerImgList = self.rotateImage(answer, answerImgList)
            else:
                pass
            self.answerImageList.nextQuestion(answer, answerImgList)
        elif (self.currentLesson == "kaKha"  or self.currentLesson == "aaa") and self.gameType == "Char":
            answer, answerList = findDifferenceUtils.nextFindDifferenceQuestionWithoutImage(self.currentLesson, self.gameType)
            self.answerImageList.nextQuestion(answer, answerList)
        elif (self.currentLesson == "kaKha"  or self.currentLesson == "aaa") and self.gameType == "Img":
            answer, answerImgList =findDifferenceUtils.nextFindDifferenceQuestion(self.currentLesson, self.gameType)
            answerImgList = resizeImage(answerImgList, 65)
            self.answerImageList.nextQuestion(answer, answerImgList)

    def rotateImage(self, answer, answerImageList):
        answerImageList[int(answer)] = answerImageList[int(answer)].Rotate90()
        answerImageList[int(answer)] = answerImageList[int(answer)].Rotate90()
        return answer, answerImageList

###pure wx way to reduce image, but does not work below 2.8.8.1. Can use it later
##def resizeImage0(imageList, resizePercent):
##    print imageList
##    newImageList = []
##    for i in imageList:        
##        temp = wx.Bitmap(i, wx.BITMAP_TYPE_PNG)
##        w, h = temp.GetWidth(), temp.GetHeight()
##        temp = temp.ConvertToImage()
##        w, h = (resizePercent*w)/100, (resizePercent*h)/100
##        newImageList.append(temp.Rescale(w, h, wx.IMAGE_QUALITY_NORMAL))
##    return newImageList

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
