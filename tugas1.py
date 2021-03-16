import dian
import wx

class form(dian.MyFrame1):
    def __init__(self,parent):
        dian.MyFrame1.__init__(self,parent)

app = wx.App()
frame = form (parent=None)
frame.Show()
app.MainLoop()