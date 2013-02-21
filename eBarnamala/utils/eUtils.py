import conf.loadData as loadData
import conf.loadDataAboveNine as loadDataAboveNine 
import conf.config as config
import os
from os.path import join
import Image
import ImageDraw
import wx
import random

kaKhaStr = loadData.kaKhaStr
aaaStr = loadData.aaaStr
numberStr = loadData.numberStr
numberAboveNineStr = loadDataAboveNine.numberStr

timeStr = loadData.timeStr
baseDir = config.baseImagePath
letterImgDir = config.letterImagesPath
sworLetterImgDir = config.sworImagesPath
byanjanLetterImgDir = config.byanjanImagesPath
numberImgDir = config.numberImagesPath
timeImgDir = config.timeImagesPath
notesImgDir = config.notesImagesPath
coinsImgDir = config.coinsImagesPath

def setDataObject(currentLesson, imgInfo):
    letterList = []
    imageObject = []
    pathToImg = ''
    if currentLesson =="kaKha":
        letterList = kaKhaStr
        imageObject = loadData.kaKhaImageObject
        pathToImg = join(byanjanLetterImgDir, imgInfo)
    if currentLesson == "aaa":
        letterList = aaaStr
        imageObject = loadData.aaaImageObject
        pathToImg = join(sworLetterImgDir, imgInfo)
    if currentLesson == "oneTwo":
        letterList = numberStr
        imageObject = loadData.numberImageObject
        pathToImg = join(numberImgDir, imgInfo)
    if currentLesson == "time":
        letterList = timeStr
        imageObject = loadData.timeImageObject
        pathToImg = join(timeImgDir, imgInfo)
    if currentLesson == "elevenTwelve":
        letterList = numberAboveNineStr
    return letterList, imageObject, pathToImg


def nextLetter(currentLesson, currentLetterPosition):
    nextLetter = ''
    nextLetterPosition = 0
    imageObject = ''
    letterList = ''
    if currentLesson =="kaKha": letterList = kaKhaStr
    if currentLesson == "aaa": letterList = aaaStr
    if currentLesson == "oneTwo": letterList = numberStr
    if currentLesson == "time": letterList = timeStr
    if currentLesson == "elevenTwelve": letterList = numberAboveNineStr
    if currentLetterPosition < int(len(letterList) - 1):
        nextLetterPosition = currentLetterPosition + 1
        nextLetter = letterList[nextLetterPosition]
    else:
        nextLetterPosition = 0
        nextLetter = letterList[nextLetterPosition]
    return nextLetter, nextLetterPosition

def previousLetter(currentLesson, currentLetterPosition):
    previousLetter = ''
    previousLetterPosition = 0
    if currentLesson =="kaKha": letterList = kaKhaStr
    if currentLesson == "aaa": letterList = aaaStr
    if currentLesson == "oneTwo": letterList = numberStr
    if currentLesson == "time": letterList = timeStr
    if currentLesson == "elevenTwelve": letterList = numberAboveNineStr
    if currentLetterPosition > 0:
        previousLetterPosition = currentLetterPosition - 1
        previousLetter = letterList[previousLetterPosition]
    else:
        previousLetterPosition = len(letterList) - 1
        previousLetter = letterList[previousLetterPosition]
    return previousLetter, previousLetterPosition

def nextImage(currentLesson, imgInfo):
    pathToImg = ''
    imageObject = ''
    imgList = []
    newImg = ''
    newImageName = ''
    letterList, imageObject, pathToImg = setDataObject(currentLesson, str(imgInfo[0]))
    for root, dirs, files in os.walk(pathToImg):
        if root != '':
            imgList = [i for i in files if i[-3:] == 'png']
            if len(imgList) != 0:
                newImageName = imgList[0]
                newImg = join(pathToImg, imgList[0])
            else:
                newImg = ''
        else:
            newImg = ''
    if newImg != '':
        temp = newImageName[0:newImageName.index('.')]
        newImageName = imageObject[int(imgInfo[0])][temp]
    else:
        pass
    return newImg, newImageName, imgInfo

def nextAboveNineImage(currentLesson, currentNumber):
    numberName = ''
    number = int(loadDataAboveNine.mreplace(currentNumber, loadDataAboveNine.nepaliStr, loadDataAboveNine.englishStr))
    baseImg = Image.open(loadDataAboveNine.blankImg)
    repeatImg = Image.open(loadDataAboveNine.numberImg)
    numberNameList = loadDataAboveNine.numberAboveNineNames
    currentXPos, currentYPos = loadDataAboveNine.startX, loadDataAboveNine.startY
    posCounter = 0
    numberName = numberNameList[number - 10] #done to bring the pointer to beginning of list
    baseImg.paste(config.backgroundColour, [0,0,baseImg.size[0],baseImg.size[1]])
    draw = ImageDraw.Draw(baseImg)
    for i in range(number):
        #draw.ellipse([currentXPos, currentYPos, currentXPos + 20, currentYPos + 20], fill=config.fillColour)
        draw.bitmap((currentXPos, currentYPos), repeatImg, config.fillColour)
        #baseImg.paste(repeatImg.convert('RGB'), (currentXPos, currentYPos))
        if posCounter < 4:
            posCounter = posCounter + 1
            currentXPos =  currentXPos + loadDataAboveNine.deltaX
            currentYPos = currentYPos
        else:
            posCounter = 0
            currentXPos = 10
            currentYPos = currentYPos + loadDataAboveNine.deltaY
    del draw
    returnImg = wx.EmptyImage(loadDataAboveNine.imgSizeX, loadDataAboveNine.imgSizeY)
    returnImg.SetData(baseImg.convert('RGB').tostring())
    return returnImg, numberName 
    

def nextWordImage(currentLesson, imgInfo):
    letterList = []
    imageObject = []
    pathToImg = ''
    letterList, imageObject, pathToImg = setDataObject(currentLesson, str(imgInfo[0]))
    imgLetter = int(imgInfo[0])
    imgPosition = int(imgInfo[1])
    newImg = ''
    newImageName = ''
    for root, dirs, files in os.walk(pathToImg):
        if root != '':
            imgList = [i for i in files if i[-3:] == 'png']
            if imgPosition < len(imgList)-1:
                newImg = join(pathToImg, imgList[imgPosition])
                newImageName = imgList[imgPosition]
                imgPosition = imgPosition + 1
            else:
                if len(imgList) != 0:
                    newImg = join(pathToImg, imgList[imgPosition])
                    newImageName = imgList[imgPosition]
                    imgPosition = 0
                else:
                    pass
        else:
            newImg = ''
    if newImg != '':
        temp = 0
        temp = newImageName[0:newImageName.index('.')]
        newImageName = imageObject[int(imgInfo[0])][temp]
    else:
        pass
    imgInfo[1] = imgPosition
    return newImg, newImageName, imgInfo

def nextBarakhariCombo(currentLesson, charInfo):
    returnData = []
    kaKhaList = loadData.kaKhaStr
    aaaList = loadData.aaaStr
    matraList = loadData.matraStr
    if charInfo < len(matraList)-1:
        charInfo = charInfo + 1
    else:
        charInfo = 0
    for i in range(4):
        if charInfo == 0:
            returnData.append(kaKhaList[i] + "-" + aaaList[charInfo] + "-" + matraList[charInfo] + "-" + kaKhaList[i])
        elif charInfo == 2:
            returnData.append(kaKhaList[i] + "-" + aaaList[charInfo] + "-" + matraList[charInfo] + "-" + matraList[charInfo]+kaKhaList[i])
        else:
            returnData.append(kaKhaList[i] + "-" + aaaList[charInfo] + "-" + matraList[charInfo] + "-" + kaKhaList[i]+matraList[charInfo])
    return returnData, charInfo

def previousBarakhariCombo(currentLesson, charInfo):
    returnData = []
    kaKhaList = loadData.kaKhaStr
    aaaList = loadData.aaaStr
    matraList = loadData.matraStr
    if charInfo > 0:
        charInfo = charInfo - 1
    else:
        charInfo = len(matraList)-1
    for i in range(4):
        if charInfo == 0:
            returnData.append(kaKhaList[i] + "-" + aaaList[charInfo] + "-" + matraList[charInfo] + "-" + kaKhaList[i])
        elif charInfo == 2:
            returnData.append(kaKhaList[i] + "-" + aaaList[charInfo] + "-" + matraList[charInfo] + "-" + matraList[charInfo]+kaKhaList[i])
        else:
            returnData.append(kaKhaList[i] + "-" + aaaList[charInfo] + "-" + matraList[charInfo] + "-" + kaKhaList[i]+matraList[charInfo])
    return returnData, charInfo
