import Image
import ImageDraw
import wx
import random
import conf.config as config
import conf.loadDataArithmetic as loadDataArithmetic

def nextNumber(currentLesson, currentNumber):
    nextNumber = 0
    if currentLesson == "oneMore":
        if int(currentNumber) < 20:
            nextNumber = int(currentNumber) + 1
        else:
            currentNumber = 0
            nextNumber = 1
    elif currentLesson == "oneLess":
        nextNumber = int(currentNumber) - 1
    return nextNumber, currentNumber

def previousNumber(currentLesson, currentNumber):
    previousNumber = 0
    if currentLesson == "oneMore":
        if int(currentNumber) > 0:
            currentNumber = int(currentNumber) - 1
            previousNumber = int(currentNumber) + 1
        else:
            currentNumber = 19
            previousNumber = 20
        return previousNumber, currentNumber
    if currentLesson == "oneLess":
        nextNumber = int(currentNumber) - 1
        return nextNumber, currentNumber

def nextNumberArithmetic(currentLesson):
    number = random.choice(range(1,9,1))
    numberArithmetic = random.choice(range(1,9,1))
    if (currentLesson == "simpleMinus") and (numberArithmetic > number):
        temp = numberArithmetic
        numberArithmetic = number
        number = temp
    if currentLesson == "simplePlus":
        numberAfterArithmetic = number + numberArithmetic # replace sign by operator based on currentLesson
    if currentLesson == "simpleMinus":
        numberAfterArithmetic = number - numberArithmetic
    return number, numberArithmetic, numberAfterArithmetic

def previousNumberArithmetic(currentLesson):
    number, numberArithmetic, numberAfterArithmetic = nextNumberArithmetic(currentLesson)
    return number, numberArithmetic, numberAfterArithmetic

def nextImage(currentLesson, reqNumber):
    numberName, repeatImg = '', ''
    baseImg = Image.open(loadDataArithmetic.blankImg)
    if reqNumber == 0 or reqNumber < 3:
        repeatImg = Image.open(loadDataArithmetic.numberBigImg)
    elif reqNumber > 2 and reqNumber < 5:
        repeatImg = Image.open(loadDataArithmetic.numberMediumImg)
    else:
        repeatImg = Image.open(loadDataArithmetic.numberSmallImg)
    currentXPos, currentYPos = loadDataArithmetic.startX, loadDataArithmetic.startY
    posCounter = 0
    deltaX, deltaY = repeatImg.size[0] + 5, repeatImg.size[1] + 5
    baseImg.paste(config.backgroundColour, [0,0,baseImg.size[0],baseImg.size[1]])
    draw = ImageDraw.Draw(baseImg)
    for i in range(reqNumber):
        draw.bitmap((currentXPos, currentYPos), repeatImg, config.fillColour)
        #baseImg.paste(repeatImg.convert('RGB'), (currentXPos, currentYPos))
        if posCounter < 4:
            posCounter = posCounter + 1
            currentXPos =  currentXPos + deltaX
            currentYPos = currentYPos
        else:
            posCounter = 0
            currentXPos = 10
            currentYPos = currentYPos + deltaY
    returnNumberImg = wx.EmptyImage(loadDataArithmetic.imgSizeX, loadDataArithmetic.imgSizeY)
    returnNumberImg.SetData(baseImg.convert('RGB').tostring())
    return returnNumberImg 
