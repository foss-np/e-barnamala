import wx
from wx.html import *
import os

class helpDialog(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wx.ID_ANY, name='', parent=prnt,
              pos=wx.Point(100, 100), size=wx.Size(615, 480),
              style=wx.DEFAULT_DIALOG_STYLE, title='About')
        self.SetClientSize(wx.Size(607, 453))

        self.helpMenuStaticBox = wx.StaticBox(id=wx.ID_ANY,
              label=u'', name=u'helpMenuStaticBox', parent=self, pos=wx.Point(8,
              0), size=wx.Size(592, 48), style=0)

        self.aboutButton = wx.Button(id=wx.ID_ANY,
              label=u'About', name=u'aboutButton', parent=self,
              pos=wx.Point(208, 16), size=wx.Size(75, 23), style=0)
        self.aboutButton.Bind(wx.EVT_BUTTON, self.OnAboutButtonButton,
              id=self.aboutButton.GetId())

        self.helpStaticBox = wx.StaticBox(id=wx.ID_ANY,
              label=u'About', name=u'helpStaticBox', parent=self,
              pos=wx.Point(8, 56), size=wx.Size(592, 392), style=0)

        self.htmlWindow = HtmlWindow(self, 123, pos=wx.Point(12,72), size = wx.Size(583, 371))
        self.htmlWindow.SetBorders(0)
        self.htmlWindow.LoadPage(os.path.join('help','about.html'))

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnAboutButtonButton(self, event):
        blankHtml = ""
        self.htmlWindow.SetPage(blankHtml)
        self.htmlWindow.LoadPage('about.html')
