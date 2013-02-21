import conf.loadDataColours as loadDataColours
import conf.loadDataAnimals as loadDataAnimals
import conf.loadData as loadData
import conf.config as config
import os
from os.path import join
import random


def charSetToUse(currentLesson):
    if currentLesson == "colour":
        englishStr = loadDataColours.colourNameEnglish
        nepaliStr = loadDataColours.colourNameNepali
    if currentLesson == "oneTwo":
        nepaliStr = loadData.numberStr
        englishStr = range(len(nepaliStr))
    if currentLesson == "time":
        nepaliStr = loadData.timeStr
        englishStr = range(len(nepaliStr))
    if currentLesson == "aaa":
        nepaliStr = loadData.aaaStr
        englishStr = range(len(nepaliStr))
    if currentLesson == "kaKha":
        nepaliStr = loadData.kaKhaStr
        englishStr = range(len(nepaliStr))
    if currentLesson == "animals":
        nepaliStr = loadDataAnimals.animalNameNepali
        englishStr = loadDataAnimals.animalNameEnglish
    return englishStr, nepaliStr

def imageDirPath(currentLesson):
    if currentLesson == "colour": imageDirPath = config.colourImagesPath
    if currentLesson == "oneTwo": imageDirPath = config.numberImagesPath
    if currentLesson == "time":   imageDirPath = config.timeImagesPath
    if currentLesson == "aaa":    imageDirPath = config.sworImagesPath
    if currentLesson == "kaKha":  imageDirPath = config.byanjanImagesPath
    if currentLesson == "animals":imageDirPath = config.animalImagesPath
    return imageDirPath

def nextRecognizeAndSearchQuestion(currentLesson):
    englishStr, nepaliStr = charSetToUse(currentLesson)
    imagePath = imageDirPath(currentLesson)
    answerList = random.sample(nepaliStr, 5)
    temp = random.sample(answerList, 1)[0]
    question = temp
    tempImgName = englishStr[nepaliStr.index(temp)]
    if currentLesson == "time":
        tempImg = join(imagePath, (str(tempImgName)))
        questionImage = join(tempImg, (str(int(tempImgName) + 1) + ".png"))
    else:
        questionImage = join(imagePath, (str(tempImgName) + ".png"))
    return question, questionImage, answerList

def nextImage(pathToImg):
    for root, dirs, files in os.walk(pathToImg):
        if root != '':
            imgList = [i for i in files if i[-3:] == 'png']
            if len(imgList) != 0:
                newImageName = random.choice(imgList)
                newImg = join(pathToImg, imgList[0])
            else:
                newImg = ''
        else:
            newImg = ''
    return newImg

def nextSearchAndRecognizeQuestion(currentLesson):
    questionList, questionImgList = [], []
    englishStr, nepaliStr = charSetToUse(currentLesson)
    imagePath = imageDirPath(currentLesson)
    if currentLesson == "oneTwo":
        questionList = random.sample(englishStr[0:len(englishStr) -1], 5)
    else:
        questionList = random.sample(englishStr, 5)
    temp = englishStr.index(random.sample(questionList, 1)[0])
    answer = nepaliStr[temp]
    for i in questionList:
        if currentLesson in ["oneTwo", "time", "aaa", "kaKha"]:
            questionImgList.append(nextImage(join(imagePath, str(i))))  
        else:
            tempImg = str(i) + ".png"
            questionImgList.append(join(imagePath, tempImg))
    for i in range(len(questionList)):
        questionList[i] = nepaliStr[englishStr.index(questionList[i])]
    return answer, questionList, questionImgList

def nextMatchImageCharQuestion(currentLesson):
    questionList, questionImgList, answerList, answerNepaliList = [], [], [], []
    englishStr, nepaliStr = charSetToUse(currentLesson)
    imagePath = imageDirPath(currentLesson)
    questionList = random.sample(englishStr, 5)
    for i in questionList:
        if currentLesson in ["oneTwo", "time", "aaa", "kaKha"]:
            answerList.append(i)
            questionImgList.append(nextImage(join(imagePath, str(i))))   
        else:
            answerList.append(i)
            tempImg = str(i) + ".png"
            questionImgList.append(join(imagePath, tempImg))
    random.shuffle(answerList)
    for i in answerList:
        answerNepaliList.append(nepaliStr[englishStr.index(i)])
    return questionList, questionImgList, answerList, answerNepaliList
