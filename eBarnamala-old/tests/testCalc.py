#!/usr/bin/python
# -*- coding: utf-8 -*-

# calculator.py

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, wx.ID_ANY, "Testing", wx.DefaultPosition, wx.Size(300, 250))
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, -1, '',  style=wx.TE_RIGHT)
        sizer.Add(self.display, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 4)

        self.formula = False

        gs = wx.GridSizer(4, 4, 3, 3)
        clearButton = wx.Button(self,wx.ID_ANY, u';\u02DAf')
        clearButton.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Aalekh'))
        clearButton.Bind(wx.EVT_BUTTON, self.OnClear)
        backButton = wx.Button(self, wx.ID_ANY, 'kl5')
        backButton.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Aalekh'))
        backButton.Bind(wx.EVT_BUTTON, self.OnBackspace)
        emptyText = wx.StaticText(self,wx.ID_ANY, '')
        closeButton = wx.Button(self,wx.ID_ANY, 'aGb')
        closeButton.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Aalekh'))
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)
        sevenButton = wx.Button(self,wx.ID_ANY, u'7')
        sevenButton.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Kalimati'))
        sevenButton.Bind(wx.EVT_BUTTON, self.OnSeven)
        eightButton = wx.Button(self,wx.ID_ANY, u'8')
        eightButton.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Kalimati'))
        eightButton.Bind(wx.EVT_BUTTON, self.OnEight)
        nineButton = wx.Button(self,wx.ID_ANY, u'9')
        nineButton.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Kalimati'))
        nineButton.Bind(wx.EVT_BUTTON, self.OnNine)
        divideButton = wx.Button(self,wx.ID_ANY, u'/')
        divideButton.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Kalimati'))
        divideButton.Bind(wx.EVT_BUTTON, self.OnDivide)
        fourButton = wx.Button(self,wx.ID_ANY, u'4')
        fourButton.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Kalimati'))
        fourButton.Bind(wx.EVT_BUTTON, self.OnFour)
        fiveButton = wx.Button(self, wx.ID_ANY, u'5')
        fiveButton.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Kalimati'))
        fiveButton.Bind(wx.EVT_BUTTON, self.OnFive)
        sixButton = wx.Button(self,wx.ID_ANY, u'6')
        sixButton.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Kalimati'))
        sixButton.Bind(wx.EVT_BUTTON, self.OnSix)
        multiplyButton = wx.Button(self,wx.ID_ANY, u'*')
        multiplyButton.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Kalimati'))
        multiplyButton.Bind(wx.EVT_BUTTON, self.OnMultiply)
        oneButton = wx.Button(self,wx.ID_ANY, u'1')
        oneButton.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Kalimati'))
        oneButton.Bind(wx.EVT_BUTTON, self.OnOne)
        twoButton = wx.Button(self,wx.ID_ANY, u'2')
        twoButton.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Kalimati'))
        twoButton.Bind(wx.EVT_BUTTON, self.OnTwo)
        threeButton = wx.Button(self,wx.ID_ANY, u'3')
        threeButton.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Kalimati'))
        threeButton.Bind(wx.EVT_BUTTON, self.OnThree)
        minusButton = wx.Button(self,wx.ID_ANY, u'-')
        minusButton.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Times'))
        minusButton.Bind(wx.EVT_BUTTON, self.OnMinus)
        zeroButton = wx.Button(self,wx.ID_ANY, u'0')
        zeroButton.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Kalimati'))
        zeroButton.Bind(wx.EVT_BUTTON, self.OnZero)
        pointButton = wx.Button(self,wx.ID_ANY, '.')
        pointButton.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Kalimati'))
        pointButton.Bind(wx.EVT_BUTTON, self.OnDot)
        equalButton = wx.Button(self,wx.ID_ANY, u'=')
        equalButton.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Kalimati'))
        equalButton.Bind(wx.EVT_BUTTON, self.OnEqual)
        plusButton = wx.Button(self,wx.ID_ANY, u'+')
        plusButton.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Kalimati'))
        plusButton.Bind(wx.EVT_BUTTON, self.OnPlus)
        gs.Add(clearButton, 0, wx.EXPAND)
        gs.Add(backButton, 0, wx.EXPAND)
        gs.Add(emptyText, 0, wx.EXPAND)
        gs.Add(closeButton, 0, wx.EXPAND)
        gs.Add(sevenButton, 0, wx.EXPAND)
        gs.Add(eightButton, 0, wx.EXPAND)
        gs.Add(nineButton, 0, wx.EXPAND)
        gs.Add(divideButton, 0, wx.EXPAND)
        gs.Add(fourButton, 0, wx.EXPAND)
        gs.Add(fiveButton, 0, wx.EXPAND)
        gs.Add(sixButton, 0, wx.EXPAND)
        gs.Add(multiplyButton, 0, wx.EXPAND)
        gs.Add(oneButton, 0, wx.EXPAND)
        gs.Add(twoButton, 0, wx.EXPAND)
        gs.Add(threeButton, 0, wx.EXPAND)
        gs.Add(minusButton, 0, wx.EXPAND)
        gs.Add(zeroButton, 0, wx.EXPAND)
        gs.Add(pointButton, 0, wx.EXPAND)
        gs.Add(equalButton, 0, wx.EXPAND)
        gs.Add(plusButton, 0, wx.EXPAND)

        sizer.Add(gs, 1, wx.EXPAND)

        self.SetSizer(sizer)
        self.Centre()

    def SetWindowShape(self, event):
        r = wx.RegionFromBitmap(self.bmp)
        self.hasShape = self.SetShape(r)

    def OnClear(self, event):
        self.display.Clear()

    def OnBackspace(self, event):
        formula = self.display.GetValue()
        self.display.Clear()
        self.display.SetValue(formula[:-1])

    def OnClose(self, event):
        self.Close()

    def OnDivide(self, event):
        if self.formula:
            return
        self.display.AppendText(u'/')

    def OnMultiply(self, event):
        if self.formula:
            return
        self.display.AppendText(u'*')
        
    def OnMinus(self, event):
        if self.formula:
            return
        self.display.AppendText(u'-')

    def OnPlus(self, event):
        if self.formula:
            return
        self.display.AppendText(u'+')

    def OnDot(self, event):
        if self.formula:
            return
        self.display.AppendText(u'.')

    def OnEqual(self, event):
        if self.formula:
            return
        formula = self.display.GetValue()
        self.formula = False
        try:
            self.display.Clear()
            output = eval(formula)
            self.display.AppendText(str(output))
        except StandardError:
            self.display.AppendText("Error")

    def OnZero(self, event):
        if self.formula:
            self.display.Clear()
            self.formula = False
        self.display.AppendText(u'0')

    def OnOne(self, event):
        if self.formula:
            self.display.Clear()
            self.formula = False
        self.display.AppendText(u'1')

    def OnTwo(self, event):
        if self.formula:
            self.display.Clear()
            self.formula = False
        self.display.AppendText(u'2')

    def OnThree(self, event):
        if self.formula:
            self.display.Clear()
            self.formula = False
        self.display.AppendText(u'3')

    def OnFour(self, event):
        if self.formula:
            self.display.Clear()
            self.formula = False
        self.display.AppendText(u'4')

    def OnFive(self, event):
        if self.formula:
            self.display.Clear()
            self.formula = False
        self.display.AppendText(u'5')

    def OnSix(self, event):
        if self.formula:
            self.display.Clear()
            self.formula = False
        self.display.AppendText(u'6')

    def OnSeven(self, event):
        if self.formula:
            self.display.Clear()
            self.formula = False
        self.display.AppendText(u'7')

    def OnEight(self, event):
        if self.formula:
            self.display.Clear()
            self.formula = False
        self.display.AppendText(u'8')

    def OnNine(self, event):
        if self.formula:
            self.display.Clear()
            self.formula = False
        self.display.AppendText(u'9')

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

app = MyApp(0)
app.MainLoop()
