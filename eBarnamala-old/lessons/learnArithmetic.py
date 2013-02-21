import wx
import conf.config as config
import utils.arithmeticUtils as arithmeticUtils
import conf.loadDataArithmetic as loadDataArithmetic
import utils.bottomMenu as bottomMenu
import conf.messages as messages
from os.path import join

class learnArithmeticPanel(wx.Panel):
    def __init__(self, parent, id, mainPanel):
        self.englishNumberArray = ['0','1','2','3','4','5','6','7','8','9']
        self.nepaliNumberArray = loadDataArithmetic.numberStr
        self.currentNumber = 0
        self.nextNumber = 0
        self.numberArithmetic = 0
        self.currentLesson = "oneMore"
        self.mainWin = mainPanel

        self.menuPanel = wx.Panel(parent, wx.ID_ANY, (0, 0), (800, 100))
        self.menuPanel.SetBackgroundColour(config.backgroundColour)

        oneMoreImg = wx.Bitmap(join(config.buttonsPath,'oneMore.png'), wx.BITMAP_TYPE_PNG)
        self.oneMoreButton = wx.BitmapButton(self.menuPanel, wx.ID_ANY, oneMoreImg, (50,10), style = wx.NO_BORDER)
        self.oneMoreButton.SetBackgroundColour(config.backgroundColour)
        self.oneMoreButton.Bind(wx.EVT_BUTTON, self.OnOneMoreButton, id=self.oneMoreButton.GetId())

        oneLessImg = wx.Bitmap(join(config.buttonsPath,'oneLess.png'), wx.BITMAP_TYPE_PNG)
        self.oneLessButton = wx.BitmapButton(self.menuPanel, wx.ID_ANY, oneLessImg, (200,10), style = wx.NO_BORDER)
        self.oneLessButton.SetBackgroundColour(config.backgroundColour)
        self.oneLessButton.Bind(wx.EVT_BUTTON, self.OnOneLessButton, id=self.oneLessButton.GetId())

        simplePlusImg = wx.Bitmap(join(config.buttonsPath,'simplePlus.png'), wx.BITMAP_TYPE_PNG)
        self.simplePlusButton = wx.BitmapButton(self.menuPanel, wx.ID_ANY, simplePlusImg, (350,10), style = wx.NO_BORDER)
        self.simplePlusButton.SetBackgroundColour(config.backgroundColour)
        self.simplePlusButton.Bind(wx.EVT_BUTTON, self.OnSimplePlusButton, id=self.simplePlusButton.GetId())

        simpleMinusImg = wx.Bitmap(join(config.buttonsPath,'simpleMinus.png'), wx.BITMAP_TYPE_PNG)
        self.simpleMinusButton = wx.BitmapButton(self.menuPanel, wx.ID_ANY, simpleMinusImg, (500,10), style = wx.NO_BORDER)
        self.simpleMinusButton.SetBackgroundColour(config.backgroundColour)
        self.simpleMinusButton.Bind(wx.EVT_BUTTON, self.OnSimpleMinusButton, id=self.simpleMinusButton.GetId())

        self.displayPanel = wx.Panel(parent, wx.ID_ANY, (0, 100), (800, 500))
        self.displayPanel.SetBackgroundColour(config.backgroundColour)

        self.displayLabel0 = wx.StaticText(self.displayPanel, wx.ID_ANY, messages.number, (80, 110), style = wx.ALIGN_CENTRE)
        self.displayLabel0.SetFont(wx.Font(config.fontSize[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayLabel1 = wx.StaticText(self.displayPanel, wx.ID_ANY, messages.oneMoreLabel, (320, 110), style = wx.ALIGN_CENTRE)
        self.displayLabel1.SetFont(wx.Font(config.fontSize[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayLabel2 = wx.StaticText(self.displayPanel, wx.ID_ANY, messages.upNumberLabel, (540, 110), style = wx.ALIGN_CENTRE)
        self.displayLabel2.SetFont(wx.Font(config.fontSize[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))

        self.nextNumber, self.currentNumber = arithmeticUtils.nextNumber(self.currentLesson, self.currentNumber)
        self.displayLabel3 = wx.StaticText(self.displayPanel, wx.ID_ANY, self.mreplace(str(self.currentNumber), "engToNep"), (80, 160), style = wx.ALIGN_CENTRE)
        self.displayLabel3.SetFont(wx.Font(config.fontSize[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontNameArithmetic))
        self.displayLabel4 = wx.StaticText(self.displayPanel, wx.ID_ANY, " + ", (220, 160), style = wx.ALIGN_CENTRE)
        self.displayLabel4.SetFont(wx.Font(config.fontSize[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontNameArithmetic))
        self.displayLabel5 = wx.StaticText(self.displayPanel, wx.ID_ANY, self.mreplace(str(1), "engToNep"), (360, 160), style = wx.ALIGN_CENTRE)
        self.displayLabel5.SetFont(wx.Font(config.fontSize[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontNameArithmetic))
        self.displayLabel6 = wx.StaticText(self.displayPanel, wx.ID_ANY, " = ", (470, 160), style = wx.ALIGN_CENTRE)
        self.displayLabel6.SetFont(wx.Font(config.fontSize[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontNameArithmetic))
        self.displayLabel7 = wx.StaticText(self.displayPanel, wx.ID_ANY, self.mreplace(str(self.nextNumber), "engToNep"), (580, 160), style = wx.ALIGN_CENTRE)
        self.displayLabel7.SetFont(wx.Font(config.fontSize[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontNameArithmetic))
        
        ###Display the image based arithmetic
        currentImg = arithmeticUtils.nextImage(self.currentLesson, self.currentNumber)
        nextImg = arithmeticUtils.nextImage(self.currentLesson, self.nextNumber)
        currentNumberImg = wx.BitmapFromImage(currentImg)
        self.currentNumberImage = wx.StaticBitmap(self.displayPanel, -1, currentNumberImg, (50,230), (currentNumberImg.GetWidth(), currentNumberImg.GetHeight()))
        
        self.arithmeticSignLabel = wx.StaticText(self.displayPanel, wx.ID_ANY, " + ", (220, 230), style = wx.ALIGN_CENTRE)
        self.arithmeticSignLabel.SetFont(wx.Font(config.fontSize[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontNameArithmetic))

        nextImg = arithmeticUtils.nextImage(self.currentLesson, 1)
        numberArithmeticImg = wx.BitmapFromImage(nextImg)
        self.numberArithmeticImage = wx.StaticBitmap(self.displayPanel, -1, numberArithmeticImg, (360,230), (numberArithmeticImg.GetWidth(), numberArithmeticImg.GetHeight()))

        self.equalToLabel = wx.StaticText(self.displayPanel, wx.ID_ANY, " = ", (470, 230), style = wx.ALIGN_CENTRE)
        self.equalToLabel.SetFont(wx.Font(config.fontSize[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontNameArithmetic))
        
        nextNumberImg = wx.BitmapFromImage(nextImg)
        self.nextNumberImage = wx.StaticBitmap(self.displayPanel, -1, nextNumberImg, (570,230), (nextNumberImg.GetWidth(), nextNumberImg.GetHeight()))

        self.displayLabel8 = wx.StaticText(self.displayPanel, wx.ID_ANY, loadDataArithmetic.numberNames[int(self.currentNumber)], (80, 330), style = wx.ALIGN_CENTRE)
        self.displayLabel8.SetFont(wx.Font(config.fontSize[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayLabel9 = wx.StaticText(self.displayPanel, wx.ID_ANY, " + ", (220, 310), style = wx.ALIGN_CENTRE)
        self.displayLabel9.SetFont(wx.Font(config.fontSize[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontNameArithmetic))
        self.displayLabel10 = wx.StaticText(self.displayPanel, wx.ID_ANY, loadDataArithmetic.numberNames[1], (360, 330), style = wx.ALIGN_CENTRE)
        self.displayLabel10.SetFont(wx.Font(config.fontSize[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))
        self.displayLabel11 = wx.StaticText(self.displayPanel, wx.ID_ANY, " = ", (470, 310), style = wx.ALIGN_CENTRE)
        self.displayLabel11.SetFont(wx.Font(config.fontSize[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontNameArithmetic))
        self.displayLabel12 = wx.StaticText(self.displayPanel, wx.ID_ANY, loadDataArithmetic.numberNames[int(self.nextNumber)], (580, 330), style = wx.ALIGN_CENTRE)
        self.displayLabel12.SetFont(wx.Font(config.fontSize[0], wx.SWISS, wx.NORMAL, wx.NORMAL, False, config.fontName))

        ###End of image based arithmetic
        
        previousArrowImg = wx.Bitmap(join(config.coreImagesPath,'previousArrow.png'), wx.BITMAP_TYPE_PNG)
        self.previousArrowButton = wx.BitmapButton(self.displayPanel, wx.ID_ANY, previousArrowImg, (50,0), style = wx.NO_BORDER)
        self.previousArrowButton.SetBackgroundColour(config.backgroundColour)
        self.previousArrowButton.Bind(wx.EVT_BUTTON, self.OnPreviousArrow, id=self.previousArrowButton.GetId())

        nextArrowImg = wx.Bitmap(join(config.coreImagesPath,'nextArrow.png'), wx.BITMAP_TYPE_PNG)
        self.nextArrowButton = wx.BitmapButton(self.displayPanel, wx.ID_ANY, nextArrowImg, (650,0), style = wx.NO_BORDER)
        self.nextArrowButton.SetBackgroundColour(config.backgroundColour)
        self.nextArrowButton.Bind(wx.EVT_BUTTON, self.OnNextArrow, id=self.nextArrowButton.GetId())

        bottomMenu.bottomMenu([self.displayPanel, self.menuPanel], parent, self.mainWin, 'twoButton')

    def OnOneMoreButton(self, event):
        self.currentLesson = "oneMore"
        self.arithmeticSignLabel.SetLabel("+")
        self.currentNumber = 0
        self.displayLabel1.SetLabel(messages.oneMoreLabel)
        self.displayLabel2.SetLabel(messages.upNumberLabel)
        self.nextNumber, self.currentNumber = arithmeticUtils.nextNumber(self.currentLesson, self.currentNumber)
        self.displayLabel3.SetLabel(self.mreplace(str(self.currentNumber), "engToNep"))
        self.displayLabel4.SetLabel("+")
        self.displayLabel9.SetLabel("+")
        self.displayLabel5.SetLabel(self.mreplace(str(1), "engToNep"))
        self.displayLabel7.SetLabel(self.mreplace(str(self.nextNumber), "engToNep"))
        currentImg = arithmeticUtils.nextImage(self.currentLesson, self.currentNumber)
        nextImg = arithmeticUtils.nextImage(self.currentLesson, self.nextNumber)
        self.currentNumberImage.SetBitmap(wx.BitmapFromImage(currentImg))
        numberArithmeticImg = arithmeticUtils.nextImage(self.currentLesson, 1)
        self.numberArithmeticImage.SetBitmap(wx.BitmapFromImage(numberArithmeticImg))
        self.nextNumberImage.SetBitmap(wx.BitmapFromImage(nextImg))
        self.displayLabel8.SetLabel(loadDataArithmetic.numberNames[int(self.currentNumber)])
        self.displayLabel10.SetLabel(loadDataArithmetic.numberNames[1])
        self.displayLabel12.SetLabel(loadDataArithmetic.numberNames[int(self.nextNumber)])

    def OnOneLessButton(self, event):
        self.currentLesson = "oneLess"
        self.arithmeticSignLabel.SetLabel("-")
        self.currentNumber = 1
        self.numberForOneLess = 1
        self.displayLabel1.SetLabel(messages.oneLessLabel)
        self.displayLabel2.SetLabel(messages.downNumberLabel)
        self.nextNumber, self.currentNumber = arithmeticUtils.nextNumber(self.currentLesson, self.currentNumber)
        self.displayLabel3.SetLabel(self.mreplace(str(self.currentNumber), "engToNep"))
        self.displayLabel4.SetLabel("-")
        self.displayLabel9.SetLabel("-")
        self.displayLabel5.SetLabel(self.mreplace(str(1), "engToNep"))
        self.displayLabel7.SetLabel(self.mreplace(str(self.nextNumber), "engToNep"))
        currentImg = arithmeticUtils.nextImage(self.currentLesson, self.currentNumber)
        nextImg = arithmeticUtils.nextImage(self.currentLesson, self.nextNumber)
        self.currentNumberImage.SetBitmap(wx.BitmapFromImage(currentImg))
        numberArithmeticImg = arithmeticUtils.nextImage(self.currentLesson, 1)
        self.numberArithmeticImage.SetBitmap(wx.BitmapFromImage(numberArithmeticImg))
        self.nextNumberImage.SetBitmap(wx.BitmapFromImage(nextImg))
        self.displayLabel8.SetLabel(loadDataArithmetic.numberNames[int(self.currentNumber)])
        self.displayLabel10.SetLabel(loadDataArithmetic.numberNames[1])
        self.displayLabel12.SetLabel(loadDataArithmetic.numberNames[int(self.nextNumber)])

    def OnSimplePlusButton(self, event):
        self.currentLesson = "simplePlus"
        self.displayLabel1.SetLabel(messages.numberToAdd)
        self.displayLabel2.SetLabel(messages.afterArithmetic)
        self.arithmeticSignLabel.SetLabel("+")
        self.currentNumber, self.numberArithmetic, self.nextNumber = arithmeticUtils.nextNumberArithmetic(self.currentLesson)
        self.displayLabel3.SetLabel(self.mreplace(str(self.currentNumber), "engToNep"))
        self.displayLabel4.SetLabel("+")
        self.displayLabel9.SetLabel("+")
        self.displayLabel5.SetLabel(self.mreplace(str(self.numberArithmetic), "engToNep"))
        self.displayLabel7.SetLabel(self.mreplace(str(self.nextNumber), "engToNep"))
        currentImg = arithmeticUtils.nextImage(self.currentLesson, self.currentNumber)
        numberArithmeticImg = arithmeticUtils.nextImage(self.currentLesson, self.numberArithmetic)
        nextImg = arithmeticUtils.nextImage(self.currentLesson, self.nextNumber)
        self.currentNumberImage.SetBitmap(wx.BitmapFromImage(currentImg))
        self.numberArithmeticImage.SetBitmap(wx.BitmapFromImage(numberArithmeticImg))
        self.nextNumberImage.SetBitmap(wx.BitmapFromImage(nextImg))

        self.displayLabel8.SetLabel(loadDataArithmetic.numberNames[int(self.currentNumber)])
        self.displayLabel10.SetLabel(loadDataArithmetic.numberNames[int(self.numberArithmetic)])
        self.displayLabel12.SetLabel(loadDataArithmetic.numberNames[int(self.nextNumber)])

    def OnSimpleMinusButton(self, event):
        self.currentLesson = "simpleMinus"
        self.displayLabel1.SetLabel(messages.numberToMinus)
        self.displayLabel2.SetLabel(messages.afterArithmetic)
        self.arithmeticSignLabel.SetLabel("-")
        self.currentNumber, self.numberArithmetic, self.nextNumber = arithmeticUtils.nextNumberArithmetic(self.currentLesson)
        self.displayLabel3.SetLabel(self.mreplace(str(self.currentNumber), "engToNep"))
        self.displayLabel4.SetLabel("-")
        self.displayLabel9.SetLabel("-")
        self.displayLabel5.SetLabel(self.mreplace(str(self.numberArithmetic), "engToNep"))
        self.displayLabel7.SetLabel(self.mreplace(str(self.nextNumber), "engToNep"))
        currentImg = arithmeticUtils.nextImage(self.currentLesson, self.currentNumber)
        numberArithmeticImg = arithmeticUtils.nextImage(self.currentLesson, self.numberArithmetic)
        nextImg = arithmeticUtils.nextImage(self.currentLesson, self.nextNumber)
        self.currentNumberImage.SetBitmap(wx.BitmapFromImage(currentImg))
        self.numberArithmeticImage.SetBitmap(wx.BitmapFromImage(numberArithmeticImg))
        self.nextNumberImage.SetBitmap(wx.BitmapFromImage(nextImg))

        self.displayLabel8.SetLabel(loadDataArithmetic.numberNames[int(self.currentNumber)])
        self.displayLabel10.SetLabel(loadDataArithmetic.numberNames[int(self.numberArithmetic)])
        self.displayLabel12.SetLabel(loadDataArithmetic.numberNames[int(self.nextNumber)])

    def OnPreviousArrow(self, event):
        mathSign = ''
        if self.currentLesson == "oneLess":
            mathSign = loadDataArithmetic.mathSign[2]
            if self.numberForOneLess > 1:
                self.numberForOneLess = self.numberForOneLess - 1
            else:
                self.numberForOneLess = 20
            self.currentNumber = self.numberForOneLess
        else:
            mathSign = loadDataArithmetic.mathSign[0]
        if (self.currentLesson == "oneMore") or (self.currentLesson == "oneLess"):
            self.nextNumber, self.currentNumber = arithmeticUtils.previousNumber(self.currentLesson, self.currentNumber)
            self.displayLabel5.SetLabel(self.mreplace(str(1), "engToNep"))
            self.displayLabel10.SetLabel(loadDataArithmetic.numberNames[1])
            numberArithmeticImg = arithmeticUtils.nextImage(self.currentLesson, 1)
        if (self.currentLesson == "simplePlus") or (self.currentLesson == "simpleMinus"):
            self.currentNumber, self.numberArithmetic, self.nextNumber = arithmeticUtils.previousNumberArithmetic(self.currentLesson)
            self.displayLabel5.SetLabel(self.mreplace(str(self.numberArithmetic),"engToNep"))
            self.displayLabel10.SetLabel(loadDataArithmetic.numberNames[int(self.numberArithmetic)])
            numberArithmeticImg = arithmeticUtils.nextImage(self.currentLesson, self.numberArithmetic)
        self.displayLabel3.SetLabel(self.mreplace(str(self.currentNumber), "engToNep"))
        self.displayLabel7.SetLabel(self.mreplace(str(self.nextNumber), "engToNep"))
        currentImg = arithmeticUtils.nextImage(self.currentLesson, self.currentNumber)
        nextImg = arithmeticUtils.nextImage(self.currentLesson, self.nextNumber)
        self.currentNumberImage.SetBitmap(wx.BitmapFromImage(currentImg))
        self.numberArithmeticImage.SetBitmap(wx.BitmapFromImage(numberArithmeticImg))
        self.nextNumberImage.SetBitmap(wx.BitmapFromImage(nextImg))
        
        self.displayLabel8.SetLabel(loadDataArithmetic.numberNames[int(self.currentNumber)])
        self.displayLabel12.SetLabel(loadDataArithmetic.numberNames[int(self.nextNumber)])

    def OnNextArrow(self, event):
        mathSign = ''
        if self.currentLesson == "oneLess":
            mathSign = loadDataArithmetic.mathSign[2]
            if self.numberForOneLess < 20:
                self.numberForOneLess = self.numberForOneLess + 1
            else:
                self.numberForOneLess = 1
            self.nextNumber = self.numberForOneLess
        else:
            mathSign = loadDataArithmetic.mathSign[0]
        if (self.currentLesson == "oneMore") or (self.currentLesson == "oneLess"):
            self.nextNumber, self.currentNumber = arithmeticUtils.nextNumber(self.currentLesson, self.nextNumber)
            self.displayLabel5.SetLabel(self.mreplace(str(1), "engToNep"))
            self.displayLabel10.SetLabel(loadDataArithmetic.numberNames[1])
            numberArithmeticImg = arithmeticUtils.nextImage(self.currentLesson, 1)
        if (self.currentLesson == "simplePlus") or (self.currentLesson == "simpleMinus"):
            self.currentNumber, self.numberArithmetic, self.nextNumber = arithmeticUtils.nextNumberArithmetic(self.currentLesson)
            self.displayLabel5.SetLabel(self.mreplace(str(self.numberArithmetic),"engToNep"))
            self.displayLabel10.SetLabel(loadDataArithmetic.numberNames[int(self.numberArithmetic)])
            numberArithmeticImg = arithmeticUtils.nextImage(self.currentLesson, self.numberArithmetic)
        self.displayLabel3.SetLabel(self.mreplace(str(self.currentNumber), "engToNep"))
        self.displayLabel7.SetLabel(self.mreplace(str(self.nextNumber), "engToNep"))
        currentImg = arithmeticUtils.nextImage(self.currentLesson, self.currentNumber)
        nextImg = arithmeticUtils.nextImage(self.currentLesson, self.nextNumber)
        self.currentNumberImage.SetBitmap(wx.BitmapFromImage(currentImg))
        self.numberArithmeticImage.SetBitmap(wx.BitmapFromImage(numberArithmeticImg))
        self.nextNumberImage.SetBitmap(wx.BitmapFromImage(nextImg))
        
        self.displayLabel8.SetLabel(loadDataArithmetic.numberNames[int(self.currentNumber)])
        self.displayLabel12.SetLabel(loadDataArithmetic.numberNames[int(self.nextNumber)])

    def mreplace(self, s, toFrom):
        if toFrom == "engToNep":
            oldCharArray = self.englishNumberArray
            newCharArray = self.nepaliNumberArray
        elif toFrom == "nepToEng":
            oldCharArray = self.nepaliNumberArray
            newCharArray = self.englishNumberArray
	for a, b in zip(oldCharArray, newCharArray):
		s = s.replace(a, b)
	return s
