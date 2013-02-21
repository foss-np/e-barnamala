import wx
import conf.config as config
from os.path import join
import help.helpDialog as helpDialog

class bottomMenu():
    def __init__(self, parent, mainFrame, mainPanel, bottomReq, currentPanel = None):
        self.parent = parent
        self.mainFrame = mainFrame
        self.mainPanel = mainPanel
        self.currentPanel = currentPanel
        yPos = 0
        if len(self.parent) == 1:
            yPos = 480
        elif len(self.parent) == 2:
            yPos = 380
        else:
            yPos = 380
        if bottomReq == 'oneButton':
            quitImg = wx.Bitmap(join(config.buttonsPath,'quit.png'), wx.BITMAP_TYPE_PNG)
            self.quitButton = wx.BitmapButton(self.parent[0], wx.ID_ANY, quitImg, (100,yPos), style = wx.NO_BORDER)
            self.quitButton.SetBackgroundColour(config.backgroundColour)
            self.quitButton.Bind(wx.EVT_BUTTON, self.OnQuit, id=self.quitButton.GetId())

            aboutImg = wx.Bitmap(join(config.iconsPath,'about.png'), wx.BITMAP_TYPE_PNG)
            self.aboutButton = wx.BitmapButton(self.parent[0], wx.ID_ANY, aboutImg, (740,yPos), style = wx.NO_BORDER)
            self.aboutButton.SetBackgroundColour(config.backgroundColour)
            self.aboutButton.Bind(wx.EVT_BUTTON, self.OnAbout, id=self.aboutButton.GetId())
            
        elif bottomReq == 'twoButton':
            homeImg = wx.Bitmap(join(config.buttonsPath,'homeHalf.png'), wx.BITMAP_TYPE_PNG)
            self.homeButton = wx.BitmapButton(parent[0], wx.ID_ANY, homeImg, (100,yPos), style = wx.NO_BORDER)
            self.homeButton.SetBackgroundColour(config.backgroundColour)
            self.homeButton.Bind(wx.EVT_BUTTON, self.OnHome, id=self.homeButton.GetId())

            quitImg = wx.Bitmap(join(config.buttonsPath,'crossHalf.png'), wx.BITMAP_TYPE_PNG)
            self.quitButton = wx.BitmapButton(parent[0], wx.ID_ANY, quitImg, (405,yPos), style = wx.NO_BORDER)
            self.quitButton.SetBackgroundColour(config.backgroundColour)
            self.quitButton.Bind(wx.EVT_BUTTON, self.OnQuit, id=self.quitButton.GetId())

            aboutImg = wx.Bitmap(join(config.iconsPath,'about.png'), wx.BITMAP_TYPE_PNG)
            self.aboutButton = wx.BitmapButton(self.parent[0], wx.ID_ANY, aboutImg, (740,yPos), style = wx.NO_BORDER)
            self.aboutButton.SetBackgroundColour(config.backgroundColour)
            self.aboutButton.Bind(wx.EVT_BUTTON, self.OnAbout, id=self.aboutButton.GetId())
            
        elif bottomReq == 'threeButton':
            homeImg = wx.Bitmap(join(config.buttonsPath,'homeQuarter.png'), wx.BITMAP_TYPE_PNG)
            self.homeButton = wx.BitmapButton(parent[0], wx.ID_ANY, homeImg, (100,yPos), style = wx.NO_BORDER)
            self.homeButton.SetBackgroundColour(config.backgroundColour)
            self.homeButton.Bind(wx.EVT_BUTTON, self.OnHome, id=self.homeButton.GetId())

            backImg = wx.Bitmap(join(config.buttonsPath,'backQuarter.png'), wx.BITMAP_TYPE_PNG)
            self.backButton = wx.BitmapButton(parent[0], wx.ID_ANY, backImg, (317,yPos), style = wx.NO_BORDER)
            self.backButton.SetBackgroundColour(config.backgroundColour)
            self.backButton.Bind(wx.EVT_BUTTON, self.OnBack, id=self.backButton.GetId())

            quitImg = wx.Bitmap(join(config.buttonsPath,'crossQuarter.png'), wx.BITMAP_TYPE_PNG)
            self.quitButton = wx.BitmapButton(parent[0], wx.ID_ANY, quitImg, (496,yPos), style = wx.NO_BORDER)
            self.quitButton.SetBackgroundColour(config.backgroundColour)
            self.quitButton.Bind(wx.EVT_BUTTON, self.OnQuit, id=self.quitButton.GetId())

            aboutImg = wx.Bitmap(join(config.iconsPath,'about.png'), wx.BITMAP_TYPE_PNG)
            self.aboutButton = wx.BitmapButton(self.parent[0], wx.ID_ANY, aboutImg, (740,yPos), style = wx.NO_BORDER)
            self.aboutButton.SetBackgroundColour(config.backgroundColour)
            self.aboutButton.Bind(wx.EVT_BUTTON, self.OnAbout, id=self.aboutButton.GetId())

    def OnAbout(self, event):
        dlg = helpDialog.helpDialog(self.mainFrame)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnQuit(self, event):
        self.mainFrame.Destroy()

    def OnHome(self, event):
        for i in self.parent:
            i.Destroy()
        self.mainPanel.Show(True)
        self.mainFrame.SendSizeEvent()  ## SendSizeEvent only works with frame, not panel
        #self.mainPanel.SendSizeEvent() ## Used previously, but gave problem in GTK.
        #self.mainPanel.SetAutoLayout(True)

    def OnBack(self, event):
        self.parent[0].Destroy()
        self.currentPanel.Show(True)
        self.mainFrame.SendSizeEvent()
        #self.currentPanel.SendSizeEvent() ## Used previously, but gave problem in GTK.
        #self.mainPanel.SetAutoLayout(True)
