import conf.loadDataAnimals as loadDataAnimals
import conf.loadDataColours as loadDataColours
import conf.loadData as loadData
import conf.config as config
import os
from os.path import join
import random

def charSetToUse(currentLesson, gameType):
    if currentLesson == "aaa" and gameType == "Char":
        englishStrForCurrent = loadData.aaaStr
        oddLesson = 'kaKha'
        englishStrForOdd = loadData.kaKhaStr
        
    if currentLesson == "kaKha" and gameType == "Char":
        englishStrForCurrent = loadData.kaKhaStr
        oddLesson = 'aaa'
        englishStrForOdd = loadData.aaaStr

    if currentLesson == "kaKha" and gameType == "Img":
        englishStrForCurrent = range(len(loadData.kaKhaStr))
        oddLesson = 'aaa'
        englishStrForOdd = range(len(loadData.aaaStr))

    if currentLesson == "aaa" and gameType == "Img":
        englishStrForCurrent = range(len(loadData.aaaStr))
        oddLesson = 'kaKha'
        englishStrForOdd = range(len(loadData.kaKhaStr))

    if currentLesson == "colour" and gameType == "Img":
        oddLesson = 'colour'
        englishStrForCurrent = loadDataColours.colourNameEnglish
        englishStrForOdd = loadDataColours.colourNameEnglish 
        
    if currentLesson == "animals"  and gameType == "Img":
        oddLessonList = ['birds','insects']
        oddLesson = random.choice(oddLessonList)
        englishStrForCurrent = loadDataAnimals.animalNameEnglish
        if oddLesson == 'birds':
            englishStrForOdd = loadDataAnimals.birdNameEnglish
        elif oddLesson == 'insects':
            englishStrForOdd = loadDataAnimals.insectNameEnglish
            
    return englishStrForCurrent, englishStrForOdd, oddLesson

def imageDirPath(currentLesson):
    if currentLesson == "animals" : imageDirPath = config.animalImagesPath
    if currentLesson == "birds" : imageDirPath = config.birdImagesPath
    if currentLesson == "insects" : imageDirPath = config.insectImagesPath
    if currentLesson == "kaKha" : imageDirPath = config.byanjanImagesPath
    if currentLesson == "aaa" : imageDirPath = config.sworImagesPath
    if currentLesson == "colour" : imageDirPath = config.colourImagesPath
    return imageDirPath

def fileList(currentLesson, imagePath):
    imgList = []
    for root, dirs, files in os.walk(imagePath):
        if root != '':
            imgList = [i for i in files if i[-3:] == 'png']
    return join(imagePath, random.choice(imgList))

def nextFindDifferenceQuestion(currentLesson, gameType):
    answerList, answerImgList = [], []
    temp, questionImg, question = "", "", 1
    englishStrForCurrent, englishStrForOdd, oddLesson = charSetToUse(currentLesson, gameType)
    if currentLesson != "colour":
        question = random.choice(englishStrForOdd)
        answerList = random.sample(englishStrForCurrent, 4)
    else:
        answerList = random.sample(englishStrForCurrent, 5)
        question = random.choice(answerList)
        answerList.remove(question)
    if currentLesson == "animals" or currentLesson == "colour":
        temp = str(question) + ".png" 
        questionImg = join(imageDirPath(oddLesson), temp)
        for i in answerList:
            answerImgList.append(join(imageDirPath(currentLesson), (str(i) + ".png"))) 
    if currentLesson == "kaKha" or currentLesson == "aaa":
        questionImg = fileList(currentLesson, join(imageDirPath(oddLesson), str(question)))
        for i in answerList:
            answerImgList.append(fileList(currentLesson, join(imageDirPath(currentLesson), str(i))))
    answerImgList.append(questionImg)
    random.shuffle(answerImgList)
    answer = answerImgList.index(questionImg)
    return answer, answerImgList

def nextFindDifferenceQuestionWithoutImage(currentLesson, gameType):
    englishStrForCurrent, englishStrForOdd, oddLesson = charSetToUse(currentLesson, gameType)
    question = random.choice(englishStrForOdd)
    answerList = random.sample(englishStrForCurrent, 4)
    answerList.append(question)
    random.shuffle(answerList)
    answer = answerList.index(question)
    return answer, answerList
    
