'''wxPython Calculator Demo in 50 lines of code'''

# Calculator GUI:

# ___________v
# [7][8][9][/] 
# [4][5][6][*]
# [1][2][3][-]
# [0][.][C][+]
# [    =     ]

from __future__ import division # So that 8/3 will be 2.6666 and not 2
import wx
from math import * # So we can evaluate "sqrt(8)"

class Calculator(wx.Dialog):
    '''Main calculator dialog'''
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, u'\u0915\u094D\u092F\u093E\u0932\u0915\u0941\u0932\u0947\u091F\u0930')
        sizer = wx.BoxSizer(wx.VERTICAL) # Main vertical sizer

        # ____________v
        self.display = wx.ComboBox(self, -1) # Current calculation
        sizer.Add(self.display, 0, wx.EXPAND) # Add to main sizer

        # [7][8][9][/] 
        # [4][5][6][*]
        # [1][2][3][-]
        # [0][.][C][+]
        gsizer = wx.GridSizer(4, 4)
        for row in ((u'\u096D', u'\u096E', u'\u096F', '/'),
                    (u'\u096A', u'\u096B', u'\u096C', '*'),
                    (u'\u0967', u'\u0968', u'\u0969', '-'),
                    (u'\u0966', '.', u'\u092E\u0947\u091F', '+')):
            for label in row:
                b = wx.Button(self, -1, label)
		b.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Kalimati'))
                gsizer.Add(b)
                self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        sizer.Add(gsizer, 1, wx.EXPAND)

        # [    =     ]
        b = wx.Button(self, -1, "=")
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        sizer.Add(b, 0, wx.EXPAND)
        self.equal = b

        # Set sizer and center
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.CenterOnScreen()

    def OnButton(self, evt):
        '''Handle button click event'''
        # Get title of clicked button
        label = evt.GetEventObject().GetLabel()

        if label == "=": # Calculate
            try:
                compute = self.display.GetValue()
                # Add to history
                self.display.Insert(compute, 0)
                
                compute = self.mreplace(compute,"nep","eng")
                
                # Ignore empty calculation
                if not compute.strip():
                    return

                # Calculate result
                result = eval(compute)
                result = self.mreplace(str(result),"eng","nep")

                # Show result
                self.display.SetValue(result)
            except Exception, e:
                wx.LogError(str(e))
                return

        elif label == u'\u092E\u0947\u091F': # Clear
            self.display.SetValue("")

        else: # Just add button text to current calculation
            self.display.SetValue(self.display.GetValue() + label)
            self.equal.SetFocus() # Set the [=] button in focus

    def mreplace(self, s, ffrom, tto):
        englishChr = ['1','2','3','4','5','6','7','8','9','0']
        nepaliChr = [u'\u0967', u'\u0968', u'\u0969',u'\u096A', u'\u096B', u'\u096C',u'\u096D', u'\u096E', u'\u096F',u'\u0966']
        if ffrom == "eng" and tto == "nep":
            for a, b in zip(englishChr, nepaliChr):
                s = s.replace(a, b)
        if ffrom == "nep" and tto == "eng":
            for a, b in zip(nepaliChr, englishChr):
                s = s.replace(a, b)
        return s

if __name__ == "__main__":
    # Run the application
    app = wx.PySimpleApp()
    dlg = Calculator()
    dlg.ShowModal()
    dlg.Destroy()
