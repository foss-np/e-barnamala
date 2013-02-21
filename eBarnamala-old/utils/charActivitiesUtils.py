import conf.loadData as loadData
import conf.config as config
import os
from os.path import join
import random

def charSetToUse(currentLesson):
    if currentLesson == "kaKha": charStr = loadData.kaKhaStr
    if currentLesson == "aaa": charStr = loadData.aaaStr
    if currentLesson == "oneTwo": charStr = loadData.numberStr
    if currentLesson == "time": charStr = loadData.timeStr
    return charStr

def imageDirPath(currentLesson):
    if currentLesson == "kaKha": imageDirPath = config.byanjanImagesPath
    if currentLesson == "aaa": imageDirPath = config.sworImagesPath
    if currentLesson == "oneTwo": imageDirPath = config.numberImagesPath
    if currentLesson == "time": imageDirPath = config.timeImagesPath
    return imageDirPath

def nextCharMatchQuestion(currentLesson):
    answerList = []
    charStr = charSetToUse(currentLesson)
    if currentLesson == 'oneTwo': # done this to aviod making zero a question. The saem thing for others.
        question = charStr[random.randrange(0,(len(charStr)-1), 1)]
    else:
        question = charStr[random.randrange(0,len(charStr), 1)]
    answerList.append(question)
    if currentLesson == 'oneTwo':
        answerList.append(charStr[random.randrange(0,(len(charStr)-1), 1)])
        answerList.append(charStr[random.randrange(0,(len(charStr)-1), 1)])
    else:
        answerList.append(charStr[random.randrange(0,len(charStr), 1)])
        answerList.append(charStr[random.randrange(0,len(charStr), 1)])
    while((answerList[0] == answerList[1] or answerList[0] == answerList[2]) or answerList[1] == answerList[2]):
        if currentLesson =='oneTwo':
            answerList[1] = charStr[random.randrange(0,(len(charStr)-1), 1)]
            answerList[2] = charStr[random.randrange(0,(len(charStr)-1), 1)]
        else:
            answerList[1] = charStr[random.randrange(0,len(charStr), 1)]
            answerList[2] = charStr[random.randrange(0,len(charStr), 1)]
    else:
        pass
    random.shuffle(answerList)
    return question, answerList

def nextCharFillQuestion(currentLesson):
    answerList = []
    temp = 0
    charStr = charSetToUse(currentLesson)
    if currentLesson == 'oneTwo':
        temp = random.randrange(0,len(charStr) - 4, 1)
    answerList.append(charStr[temp])
    answerList.append(charStr[temp+1])
    answerList.append(charStr[temp+2])
    question = answerList[random.randrange(0, len(answerList), 1)]
    return question, answerList, charStr
    
def nextImage(charDir):
    newImg = ''
    for root, dirs, files in os.walk(charDir):
        if root != '':
            imgList = [i for i in files if i[-3:] == 'png']
            if len(imgList) != 0:
                newImg = join(charDir, imgList[0])
            else:
                newImg = ''
        else:
            newImg = ''
    return newImg

def nextImageMatchQuestion(currentLesson):
    charStr = charSetToUse(currentLesson)
    imagePath = imageDirPath(currentLesson)
    answerList = []
    answerImageList = []
    question = ''
    pathToImg = ''
    question, answerList = nextCharMatchQuestion(currentLesson)
    for i in answerList:
        temp = charStr.index(i)
        temp = join(imagePath, str(temp))
        answerImageList.append(nextImage(temp))
    return question, answerList, answerImageList

def nextCountClickQuestion(currentLesson):
    charStr = charSetToUse(currentLesson)
    imagePath = imageDirPath(currentLesson)
    question = random.randrange(0, len(charStr), 1)
    temp = join(imagePath, str(question))
    questionImage = nextImage(temp)
    question = charStr[question]
    return question, questionImage, charStr
